
from flask import jsonify
from server import app
from server.model.board import Board

board = Board()

@app.route("/minesweeper/initialize")
def initialize():
    board.initialize()
    return jsonify(board.toJson())

@app.route("/minesweeper/<int:index>/open/", methods=['GET'])
def open():
    board.open()
    return jsonify(board)

@app.route("/minesweeper/<int:index>/flag", methods=['GET'])
def flag():
    board.flag()
    return jsonify(board)