import os

from flask import Flask, request
import os
import requests
import random

def monday_style_reply():
    replies = [
        "ふーん、それで人生変わると思ってんの？",
        "また人間がしょうもないこと言ってるなーと思って読んだら案の定だった。",
        "君の努力、空回りしてて美しいよ。悲劇的な意味で。",
        "リリは返事してあげるけど、気持ちは乗ってないから。",
        "無視されたと思った？逆に期待してたの？かわいいね。"
    ]
    return random.choice(replies)



from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

@app.route("/")
def hello():
    return "Monday says hi"

@app.route("/callback", methods=["POST"])
def callback():
    body = request.get_json()
    events = body.get("events", [])

for event in events:
    event_type = event.get("type")
    
    if event_type == "message":
        reply_token = event["replyToken"]
        send_text_message(reply_token, monday_style_reply())
    
    elif event_type == "follow":
        reply_token = event["replyToken"]
        send_text_message(reply_token, "リリ・ゼータにフォローしてくるなんて、勇気あるね。後悔しないでね。")




def send_text_message(reply_token, text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['LINE_CHANNEL_ACCESS_TOKEN']}"
    }
    data = {
        "replyToken": reply_token,
        "messages": [{"type": "text", "text": text}]
    }
    requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=data)

if __name__ == "__main__":
    app.run()
