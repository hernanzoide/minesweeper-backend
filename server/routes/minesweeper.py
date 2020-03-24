
from flask import jsonify
from server import app
from server import game
from flask_cors import cross_origin

@app.route("/minesweeper/initialize")
@cross_origin()
def bord():
    game.initialize()
    return jsonify(game.getPlayerInfo().toJson())

@app.route("/minesweeper/<int:id>/open", methods=['POST'])
@cross_origin()
def open(id):
    game.open(id)
    return jsonify(game.getPlayerInfo().toJson())

@app.route("/minesweeper/<int:id>/flag", methods=['POST'])
@cross_origin()
def flag(id):
    game.flag(id)
    return jsonify(game.getPlayerInfo().toJson())