from flask import jsonify
import sqlite3
dbname = 'FeelFree.db'
def get_lend(id):
    # 貸出状態の取得
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM lend id = :id", { "id": id})
    data = []
    for row in cur:
        data.append({ "id":  row[0], "place_id": row[1], "begin_date": row[2], "end_date": row[3], "purpose":row[4]})
    conn.close()
    return jsonify(data)