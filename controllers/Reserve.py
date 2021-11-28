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
        
    bdate = keydict["begin_date"]
    edate = keydict["end_date"]
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM lend")
    for row in cur:
        bdate_check = row[2]
        edate_check = row[3]
        if (bdate_check <= bdate <= edate_check) or (bdate <= bdate_check <= edate):
            return make_response('', 406)
    cur.execute("INSERT INTO lend (place_id, begin_date, end_date, purpose) VALUES (:place_id, :begin_date, :end_date, :purpose)",
    (
    keydict['place_id'], \
    keydict['begin_date'], \
    keydict['end_date'], \
    keydict['purpose'], \
    ))
    conn.commit()
    # cur.execute("SELECT * FROM lend")
    # for row in cur:
    #     print(row)
    conn.close()    
    return make_response('', 200)