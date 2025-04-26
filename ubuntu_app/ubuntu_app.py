# Ignoring unnecessary errors and warnings for simplicity.
# ruff: noqa: B201, B104, F401

from flask import Flask 
from flask_restx import Resource, Api, reqparse 
import random 

app = Flask(__name__)
api = Api(app)

@api.route("/devnet")
class Devnet(Resource):
    def get(self):
        if random.randint(1, 3) == 1:  # nosec
            return "Something seems to be broken!", 500
        else:
            return "Hello, DevNet! All Good!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec
