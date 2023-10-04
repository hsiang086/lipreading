from flask import Flask, render_template, Response, request, redirect, url_for, flash
import test

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexee.html')

@app.route('/video_feed')
def video_feed():
    return Response(test.run_on_flask("./data/video/znJbiTVg6_M.mp4"),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# test.run("./data/video/znJbiTVg6_M.mp4")
