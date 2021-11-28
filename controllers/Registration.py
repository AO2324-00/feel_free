from flask import jsonify, request, make_response
import sqlite3

dbname = 'FeelFree.db'

def registration(request):

    # 送られてきたデータの取得
    body = request.json

    # bodyのデータがJSON形式でない場合は400を返す
    if(body is None):
        return make_response('', 400)

    # bodyのデータに必要な情報が全て含まれているかをチェック(含まれていない場合は400を返す)
    for key in body:
        if key not in ['title', 'address', 'image_url'] or body[key] is None:
            return make_response('', 400)

    # データベースに接続
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # places テーブルに title, address, image_url カラムのデータを指定して追加
    cur.execute("INSERT INTO places (title, address, image_url) VALUES (:title, :address, :image_url)", (body['title'], body['address'], body['image_url']))

    # 追加情報を反映
    conn.commit()

    cur.execute("SELECT * FROM places")
    for row in cur:
        print(row)

    # データベースとの接続を解除
    conn.close()

    # ステータス 200 (OK) を返す
    return make_response('', 200)