from flask import jsonify, request, make_response
import sqlite3

dbname = 'FeelFree.db'

def reserve(request):

    body = request.json
    if body is None:
        return make_response('', 400)

    keydict = {"place_id" : None, "begin_date" : None, "end_date" : None, "purpose" : None}

    for key in body:
        if key not in keydict or body[key] is None:
            return make_response('', 400)

        else:
            keydict[key] = body[key]

    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("INSERT INTO lend (place_id, begin_date, end_date, purpose) VALUES (:place_id, :begin_date, :end_date, :purpose)",
    (
    body['place_id'], \
    body['begin_date'], \
    body['end_date'], \
    body['purpose'], \
    ))

    conn.commit()

    # cur.execute("SELECT * FROM lend")
    # for row in cur:
    #     print(row)

    conn.close()    
    return make_response('', 200)