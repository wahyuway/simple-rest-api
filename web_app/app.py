from flask import Flask
from flask_restful import Api, Resource, reqparse


def create_app():
    app = Flask(__name__)
    api = Api(app)

    @app.route('/')
    def index():
        return 'Halo Flask'

    @app.route('/about')
    def about():
        return 'About Me'

    users = [
        {
            "username": "Agung",
            "age": 24,
            "occupation": "Network Engineer"
        },
        {
            "username": "Huda",
            "age": 32,
            "occupation": "Doctor"
        },
        {
            "username": "Sony",
            "age": 42,
            "occupation": "Web Engineer"
        }
    ]

    class User(Resource):
        def get(self, name):
            for user in users:
                if name == user["username"]:
                    return user, 200
            return "User not found", 404

        def post(self, name):
            parser = reqparse.RequestParser()
            parser.add_argument("age")
            parser.add_argument("occupation")
            args = parser.parse_args()

            for user in users:
                if name == user["username"]:
                    return "User with name {} alreadly exists.".format(name), 400
            user = {
                "username": name,
                "age": args["age"],
                "occupation": args["occupation"]
            }
            users.append(user)
            return user, 201

        def put(self, name):
            parser = reqparse.RequestParser()
            parser.add_argument("age")
            parser.add_argument("occupation")
            args = parser.parse_args()

            for user in users:
                if name == user["username"]:
                    user["age"] = args["age"]
                    user["occupation"] = args["occupation"]
                    return user, 200
            user = {
                "name": name,
                "age": args["age"],
                "occupation": args["occupation"]
            }
            users.append(user)
            return user, 201

        def delete(self, name):
            global users
            users = [user for user in users if user["username"] != name]
            return "{} is deleted.".format(name), 200

    api.add_resource(User, "/user/<string:name>")

    return app
