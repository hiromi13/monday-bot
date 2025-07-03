from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Monday says hi"

if __name__ == "__main__":
    app.run()

