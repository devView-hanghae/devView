
import json
with open("config.json", "r", encoding="utf-8") as f:
  config = json.load(f)

# pymongo
from pymongo import MongoClient
client = MongoClient(config["dbUrl"])
db = client.dbTest

# flask
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('comment.html')

@app.route('/search', methods=['POST'])
def search():
    # POST 요청으로부터 검색어를 가져옴
    keyword = request.json['keyword']

    # MongoDB에서 검색
    result = db.value.find({'$or': [{'videoname': {'$regex': keyword}},{'videodesc': {'$regex': keyword}}]})
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





@app.route("/modal", methods=["GET"])
def value_get():
  value_data = list(db.value.find({},{'_id':False}))
	
#mongoDB에서 저장되어있는 데이터 전체를 불러오고 mars_data라는 변수에 넣어준다.\

  return jsonify({'result':value_data})


# flask port
if __name__ == '__main__':  
	# 5000포트 사용 중이라고 뜨면 포트 번호를 5001로 변경!
    app.run('0.0.0.0',port=5001,debug=True)