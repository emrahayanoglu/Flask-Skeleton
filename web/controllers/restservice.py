from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from flask_restful import Resource, Api

restservice = Blueprint('restservice', __name__, url_prefix='/api/v1.0/hello')
api = Api(restservice)

class HelloService(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloService, '/')
