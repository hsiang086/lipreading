from lip_detection import Detector
import json

"""
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
"""

# resize and face correction
def run():
    jaw = Detector(img_path="./data/image/lu.png") # <try photos>
    dots = jaw.relative_pos(parts=["jaw", "mouth"])
    print(dots)

    # save dots <try it in desmos>
    with open("./dots.json", "w") as f:
        f.close()
    with open("./dots.json", "w") as f:
        dots_json = {}
        for (idx, dot) in enumerate(dots):
            dots_json[str(idx)] = {}
            dots_json[str(idx)]["latex"] = f"({dot[0]}, {dot[1]})"
        json.dump(dots_json, f, indent=4)
        f.close()

    with open("./dots.txt", "w") as f:
        f.close()
    with open("./dots.txt", "w") as f:
        for dot in dots:
            f.write(f"({dot[0]}, {dot[1]})\n")
        f.close()

run()