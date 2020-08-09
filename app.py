from flask import Flask, jsonify, Response
import time

import sounddevice

app = Flask(__name__)

start_time = time.time()


@app.route('/timediff')
def hello_world():
    return jsonify(time.time() - start_time)


@app.route('/audio')
def stream_audio():
    return 


if __name__ == '__main__':
    app.run()
