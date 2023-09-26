import math
from imutils import face_utils
import imutils
import dlib
import cv2

MAX = 1e13
FINDMAX = 0
DOTS = {
	"mouth": (48, 68),
	"right_eyebrow": (17, 22),
	"left_eyebrow": (22, 27),
	"right_eye": (36, 42),
	"left_eye": (42, 48),
	"nose": (27, 35),
	"jaw": (0, 17),
	"y-top": (27, 28),
	"y-bottom": (33, 34),
	"x-left": (31, 32),
	"x-right": (35, 36),
}

class Detector:
	def __init__(self, img_path, model_path="./models/shape_predictor_68_face_landmarks.dat"):
		self.image = imutils.resize(cv2.imread(img_path), width = 500)
		self.detector = dlib.get_frontal_face_detector()
		self.predictor = dlib.shape_predictor(model_path)
		self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
		self.rects = self.detector(self.gray, 1)
		self.dots = []

	def get_dots(self, part):
		dots = []
		part = DOTS[part]
		for rect in self.rects:
			shape = self.predictor(self.gray, rect)
			shape = face_utils.shape_to_np(shape)
			for (x, y) in shape[part[0]:part[1]]:
				dots.append((x, y))
		return dots

	def show_image_and_dots(self, part):
		dots = self.get_dots(part)
		for (x, y) in dots:
			cv2.circle(self.image, (x, y), 1, (0, 0, 255), -1)
		cv2.imshow("Output", self.image)
		cv2.waitKey(0)

	def get_distance(self, theta, dot_on_axis, dot, is_x):
		# rotation matrix
		xp_on_axis = dot_on_axis[0] * math.cos(theta) - dot_on_axis[1] * math.sin(theta)
		yp_on_axis = dot_on_axis[0] * math.sin(theta) + dot_on_axis[1] * math.cos(theta)
		xp = dot[0] * math.cos(theta) - dot[1] * math.sin(theta)
		yp = dot[0] * math.sin(theta) + dot[1] * math.cos(theta)
		return xp - xp_on_axis if is_x else yp - yp_on_axis	

	def relative_pos(self, parts=["jaw", "mouth"]):
		global FINDMAX
		pos = []
		x_axis = [self.get_dots(part="x-left")[0], self.get_dots(part="x-right")[0]]
		y_axis = [self.get_dots(part="y-top")[0], self.get_dots(part="y-bottom")[0]]
		for part in parts:
			dots = self.get_dots(part)
			for dot in dots:
				m = (x_axis[1][1] - x_axis[0][1]) / (x_axis[1][0] - x_axis[0][0]) if x_axis[1][0] - x_axis[0][0] != 0 else MAX
				theta = math.atan(m)
				x = self.get_distance(theta=-theta, dot_on_axis=y_axis[0], dot=dot, is_x=True)
				y = -1 * self.get_distance(theta=-theta, dot_on_axis=x_axis[0], dot=dot, is_x=False)
				FINDMAX = max(FINDMAX, abs(x), abs(y))
				pos.append((x, y))
		return pos / FINDMAX