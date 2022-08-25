from flask import Flask, jsonify, request
import json

import pymysql.cursors
  
app = Flask(__name__) 

@app.route('/')
def hello():
    # データベースに接続
    connection = pymysql.connect(host='localhost',user='webapp',password='qazWSX123$',database='webapp',cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # データ読み込み
    sql = "select * from product"
    cursor.execute(sql)
    result = cursor.fetchall()
    # 日本語の文字化け対策
    enc = json.dumps(result, ensure_ascii=False)
    cursor.close()
    return enc

if __name__ == '__main__':
    app.run()