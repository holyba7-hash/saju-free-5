from flask import Flask, render_template, request
import os
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    name = request.form.get("name")
    birthdate = request.form.get("birthdate")
    gender = request.form.get("gender")
    topic = request.form.get("topic")
    analysis = f"<p>{name}님의 사주 분석 결과입니다. ({birthdate}, {gender}) - 주제: {topic}</p>"
    return render_template("result.html", analysis=analysis)

if __name__ == "__main__":
    # 로컬 접속 주소
    local_url = "http://localhost:5000"

    # Replit 접속 주소 추출
    repl_slug = os.environ.get("REPL_SLUG")
    repl_owner = os.environ.get("REPL_OWNER")
    repl_region = os.environ.get("REPL_REGION", "us")
    if repl_slug and repl_owner:
        replit_url = f"https://{repl_owner}.{repl_slug}.{repl_region}.repl.co"
    else:
        replit_url = "Replit 환경이 아닙니다."

    print(f"💡 로컬 접속 주소: {local_url}")
    print(f"💡 Replit 접속 주소: {replit_url}\n")

    app.run(host="0.0.0.0", port=5000)
