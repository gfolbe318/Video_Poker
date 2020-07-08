from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api, reqparse

from random import shuffle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")


api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("num", type=int, required=True)
parser.add_argument("kept", type=str, required=False)
parser.add_argument("discarded", type=str, required=False)

# For security reasons later
parser.add_argument("key", type=str, required=False)

suits = ["H", "D", "S", "C"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class MyApi(Resource):
    def __init__(self):
        self.deck = []
        self.kept = []
        self.discarded = []

    def load_deck(self):
        for suit in suits:
            for rank in ranks:
                self.deck.append({
                    "suit": suit,
                    "rank": rank
                })

    def get(self):
        self.load_deck()
        shuffle(self.deck)
        return jsonify({
            "Response": 200,
            "cards": self.deck[:5],
            "num": parser.parse_args()
        })


api.add_resource(MyApi, '/deal/')
