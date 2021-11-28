from flask import jsonify, request, make_response
import sqlite3
dbname = 'FeelFree.db'
def reserve(request):
    return make_response('', 200)