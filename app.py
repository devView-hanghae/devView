# config.json
import json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# pymongo
from pymongo import MongoClient
client = MongoClient(config["dbUrl"])
# db = client.dbView
db = client.dbTest

# flask
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# 메인화면
@app.route('/')
def home():
  return render_template('index.html')

# 상세페이지
@app.route('/page')
def page():
  return render_template('page.html')

# 상세페이지 - 리스트 조회
@app.route("/modal", methods=["GET"])
def value_get():
  test_data = list(db.value.find({}, {'_id': False}))
  return jsonify({'result': test_data})

# 상세페이지 - 키워드 검색
@app.route("/search", methods=["POST"])
def search():
  # POST 요청으로부터 검색어를 가져옴
  keyword = request.json['keyword']
  # MongoDB에서 검색
  result = db.value.find({'videoname': {'$regex': keyword}})
  # 검색 결과를 리스트로 변환
  data = []
  for doc in result:
    data.append({
      'videoname': doc['videoname'],
      'videodesc': doc['videodesc'],
      'videolink': doc['videolink'],
    })
  # 검색 결과를 JSON 형태로 반환
  return jsonify(data)



# flask port
if __name__ == '__main__':  
	 # 5000포트 사용 중이라고 뜨면 포트 번호를 5001로 변경!
   app.run('0.0.0.0',port=5000,debug=True)