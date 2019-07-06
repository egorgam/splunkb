from flask import request, render_template, jsonify
from app import app, dashboards, log
from app.integration import DB
import time


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
#     return 'kek'
        return render_template('index.html')


@app.route('/api/dashboards', methods=['GET'])
def dboards():
        if request.method == 'GET':
            return jsonify([{'name': dashboard['name'], 'dname': dashboards.mergestr(dashboard['name']),
                               'panels': dashboards.parse(dashboard)}
                                for dashboard in dashboards.get()])

@app.route('/api/panel/<namespace>', methods=['GET'])
def dpanel(namespace):
    db = DB(namespace)
    if request.method == 'GET':
        return jsonify([event for event in db.col.find({}, {"_id": 0})])
