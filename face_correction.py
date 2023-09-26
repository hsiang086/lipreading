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
    jaw = Detector(img_path="./data/image/ryan.png") # <try photos>
    dots = jaw.relative_pos(parts=["jaw", "mouth"])
    print(dots)

    # save dots <try it in desmos>
    dots_json = {}
    for (idx, dot) in enumerate(dots):
        dots_json[str(idx)] = {}
        dots_json[str(idx)]["latex"] = f"{dot[0]}, {dot[1]}"
    with open("./dots.json", "w") as f:
        json.dump(dots_json, f, indent=4)

    # with open('static/dots.js', 'w') as f:
    #     f.write(f'dots = `{str(dots_json)}`')

    with open("./dots.txt", "w") as f:
        f.write('\n'.join([f"{dot[0]}, {dot[1]}" for dot in dots]))

run()