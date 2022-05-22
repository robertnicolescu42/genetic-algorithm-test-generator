from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import main3
# from main3 import question_list
from flask import jsonify
from flask_cors import CORS
import json
from questionsList import dataset_list
import setConfig

app = Flask(__name__)
api = Api(app)
CORS(app)


class Questions(Resource):
    def get(self):
        my_list = []
        q_list = main3.run()
        for q in q_list:
            my_list.append(q.__dict__)
        print(my_list)
        return my_list


@app.route('/config',methods = ['PUT'])
def config():
   if request.method == 'PUT':
      print(request.form)
      GD = request.form['GD']
      population_size = request.form['population_size']
      iterations_size = request.form['iterations_size']
      mutation_size = request.form['mutation_size']
      setConfig.overwrite(GD, population_size, iterations_size, mutation_size)

      return str([GD, population_size, iterations_size, mutation_size])

api.add_resource(Questions, '/questions')  # '/questions' is our entry point for Users



if __name__ == '__main__':
    app.run()  # run our Flask app
