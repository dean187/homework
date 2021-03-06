from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.





@app.route('/')
def home():
    return render_template('homework_week2.html')

@app.route('/orders', methods = ['POST'])
def write_order():
    #1. 클라이언트가 준 title, author, review 가져오기
    name_receive = request.form['name_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    phonenumber_receive = request.form['phonenumber_give']


    #2. DB에 정보 삽입하기
    doc = {
        'name' : name_receive,
        'amount' : amount_receive,
        'address' : address_receive,
        'phonenumber' : phonenumber_receive
    }
    db.orders.insert_one(doc)
    #3. 성공여부 & 성공메세지 반환하기
    return jsonify({'result':'success', 'msg': '이 요청은 post'})

@app.route('/orders', methods = ['GET'])
def read_order():
    #1. DB에서 리뷰, 정보 모두 가져오기
    orders = list(db.orders.find({}, {'_id': 0}))
    #2. 성공여부 목록 반환하기
    return jsonify({'result': 'success', 'orders': 'orders'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)