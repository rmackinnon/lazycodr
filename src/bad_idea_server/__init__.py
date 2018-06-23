#!/usr/bin/python2.7

__name__ = "bad_idea_server"
__package__ = "bad_idea_server"

from time import gmtime
import flask
from flask import request, jsonify

from .github_search import prepare_search, do_search
from .api import bad_blueprint

APP = flask.Flask(__name__)

APP.register_blueprint(bad_blueprint)
#APP.run(host="0.0.0.0", port=8081, debug=True)
