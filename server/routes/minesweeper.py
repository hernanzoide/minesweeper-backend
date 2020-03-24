
from flask import jsonify
from server import app
from server import board
from flask_cors import cross_origin

@app.route("/minesweeper/initialize")
@cross_origin()
def initialize():
    board.initialize()
    return jsonify(board.toJson())

@app.route("/minesweeper/<int:id>/open", methods=['POST'])
@cross_origin()
def open(id):
    board.open(id)
    return jsonify("{'success':true }")

@app.route("/minesweeper/<int:id>/flag", methods=['POST'])
@cross_origin()
def flag(id):
    board.flag(id)
    return jsonify("{'success':true }")