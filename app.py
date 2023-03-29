
import json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# pymongo
from pymongo import MongoClient
client = MongoClient(config["dbUrl"])
db = client.dbView

# flask
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('comment.html')

@app.route('/comment', methods=['POST'])
def comment_post():
	comment_receive = request.form['comment_give']
	rating_receive = request.form['rating_give']


	doc ={
		'comment':comment_receive,
		'rating':rating_receive
	}

	db.comment.insert_one(doc)

	return jsonify({'msg':'저장완료!'})


@app.route("/comment", methods=["GET"])
def comment_get():
    comment_data = list(db.comment.find({},{'_id':False}))
#mongoDB에서 저장되어있는 데이터 전체를 불러오고 mars_data라는 변수에 넣어준다.
    return jsonify({'result':comment_data})
#불러온 데이터를 result로 프론트에 보내준다.


# flask port
if __name__ == '__main__':  
	# 5000포트 사용 중이라고 뜨면 포트 번호를 5001로 변경!
    app.run('0.0.0.0',port=5001,debug=True)