from flask import session
from flask_restful import Resource
from .parsers import auth_parser


user = dict()


class Registration(Resource):
    def post(self):
        args = auth_parser.parse_args(strict=True)
        user['login'] = args.get('login')
        user['password'] = args.get('password')
        return "Registered successfully"


class Login(Resource):
    def post(self):
        args = auth_parser.parse_args(strict=True)
        name = args.get('login')
        password = args.get('password')
        if not name:
            return "There is no user with such name. Register please."
        if name == user.get('login') and password == user.get('password'):
            session['logged_in'] = True
            return "You are logged in!"
        else:
            return "Wrong password"


class Logout(Resource):
    def get(self):
        session['logged_in'] = False
        return "You are logged out!"
