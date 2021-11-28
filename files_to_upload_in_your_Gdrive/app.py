# app.py
from flask import Flask, render_template

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url

def index():
  return render_template('index.html',data = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10})

if __name__=="__main__":
  app.run(host="0.0.0.0", port="5000", debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run()