from flask import Flask, render_template as template
from flask_cors import CORS
import webbrowser
from threading import Timer
from face_correction import run

app = Flask(__name__)
CORS(app)
PORT = 5000
OPEN_BROWSER = True

# def get_dots():
#     dots = json.load(open("./dots.json", "r"))
#     return dots

@app.route('/')
def index():
    return template('desmos.html')

if __name__ == '__main__':
    run()
    if OPEN_BROWSER:
        def open_browser():
            webbrowser.open('http://127.0.0.1:%d' % PORT)
        Timer(1, open_browser).start()

    app.run(host='0.0.0.0', port=PORT)