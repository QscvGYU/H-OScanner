from flask_restful import Resource
from flask_restplus import Namespace
from flask import Flask, request

ns = Namespace('task')
task = {}


@ns.route('/<string:task_id>')
class TaskDemo(Resource):
    def get(self, todo_id):
        return {todo_id: task[todo_id]}

    def put(self, todo_id):
        task[todo_id] = request.form['data']
        return {todo_id: task[todo_id]}