#!/usr/bin/env python
#-*- coding: utf-8 -*-


from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
import werkzeug.exceptions as ex


class multitask(ex.HTTPException):
    code = 414
    description = '<p>more than one task</p>'

abort.mappings[414] = multitask

class Cindy(oblect):
    def __init__(self):
        self.tasks = [
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

    def test1(self):
        return "Hello test1!"

    def test2(self):
        return "Hello test2!"

    def hello(self):
        return "Hello World!"

    def get_tasks(self):
        return jsonify({'tasks': self.tasks})

    
    def get_task(self, task_id):
        task = [task for task in self.tasks if task['id'] == task_id]
        if len(task) == 0:
            #without task return 404   
            abort(404)
        elif len(task) > 1:
            abort(414)
        return jsonify({'task': task[0]})

    #format error json instead html text
    #def not_found(error):
    #    return make_response(jsonify({'error': 'Not found'}), 404)

    #@app.errorhandler(414)
    #def bad_data():
    #    return make_response(jsonify({'error': 'multi tasks'}), 414)


    """
    #@app.route('/todo/api/v1.0/add/tasks', methods=['POST'])
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



"""
if __name__ == "__main__":
    app.run(debug=True)

import flask, flask.views
app = flask.Flask(__name__)
 
class View(flask.views.MethodView):
    def get(self):
        return 'Hello World!'
 
app.add_url_rule('/', view_func=View.as_view('main'))
 
app.debug = True
app.run()
"""
