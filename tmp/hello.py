#!/usr/bin/env python
#-*- coding: utf-8 -*-


from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from cindy import Cindy 

app = Flask(__name__)
c = Cindy()

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

#add_url_rule(self, rule, endpoint=None, view_func=None, **options):
app.add_url_rule('/test1', 'test1', c.test1)
app.add_url_rule('/test2', 'test2', c.test2)
app.add_url_rule('/todo/api/v1.0/tasks', 'get_tasks', c.get_tasks, methods=['GET'])
app.add_url_rule('/todo/api/v1.0/tasks/<int:task_id>', 'get_task', c.get_task, methods=['GET'])

"""
#one router for one fun
@app.route("/")
def hello():
    return "Hello World!"


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

#use get method to get task
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        #without task return 404   
        abort(404)
    elif len(task) > 1:
       abort(414)
    return jsonify({'task': task[0]})

#format error json instead html text
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(414)
def bad_data():
    return make_response(jsonify({'error': 'multi tasks'}), 414)



@app.route('/todo/api/v1.0/add/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

"""






if __name__ == "__main__":
    app.run(debug=True)



















"""
import flask, flask.views
app = flask.Flask(__name__)
 
class View(flask.views.MethodView):
    def get(self):
        return 'Hello World!'
 
app.add_url_rule('/', view_func=View.as_view('main'))
 
app.debug = True
app.run()
"""
