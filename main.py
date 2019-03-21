from models import forecast_db, recipes_db, Menu
import json


import flask
from flask import request, jsonify

# Complete me :)



app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/resources/row/all', methods=['GET'])
def api_all():
    cursor = forecast_db.execute_sql('select * from forecast;')
    arr = []
    for row in cursor.fetchall():
      arr.append(row)
      print json.dumps(row)
      return json.dumps(row)
    


@app.route('/', methods=['GET'])
def home():
  return row
  

app.run()