from flask import Flask, render_template, request, send_file
from pdf_generator import generate_pdf
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    birthdate = request.form['birthdate']
    gender = request.form['gender']
    topic = request.form['topic']

    analysis = f"""<h3>{name}님의 사주 간단 분석</h3>
    <p>생년월일: {birthdate}</p>
    <p>성별: {gender}</p>
    <p>상담 분야: {topic}</p>
    <p>※ 심층 분석은 상담 시 진행됩니다.</p>"""

    pdf_path = generate_pdf(name, analysis)
    pdf_path_abs = os.path.abspath(pdf_path)

    return render_template('result.html', analysis=analysis, pdf_filename=os.path.basename(pdf_path_abs))

@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.abspath(filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000

    # 여기를 본인 Replit 정보로 변경
    replit_username = "your-replit-username"  # 예: honggildong
    replit_appname = "your-repl-name"         # 예: saju-consult

    replit_url = f"https://{replit_username}.{replit_appname}.repl.co"

    print(f"\n💡 로컬 접속 주소: http://localhost:{port}")
    print(f"💡 Replit 접속 주소: {replit_url}\n")

    app.run(host=host, port=port)
