from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Monday says hi"

@app.route("/callback", methods=["POST"])
def callback():
    return "OK"  # まずはテスト用に200 OKを返すだけにする

if __name__ == "__main__":
    app.run()

