from flask import Flask
from flask import render_template
import socket
import os

app = Flask(__name__)

TARGET = os.environ.get('TARGET')

@app.route("/")
def main():
    return render_template('target.html', name=socket.gethostname(), target=TARGET)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
