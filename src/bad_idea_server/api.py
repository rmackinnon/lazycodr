__name__ = "bad_idea_server.api"
__package__ = "bad_idea_server"

from github import Github

from flask.blueprints import Blueprint
from flask import request, jsonify

from .github_search import do_search, prepare_search

bad_blueprint = Blueprint("bad_blueprint", __name__)


@bad_blueprint.route('/login', methods=["POST"])
def login():
    print("Got login request:")
    _json = request.get_json()
    _user = _json["data"]["username"]
    _passwd = _json["data"]["passwd"]
    _user = "demo-lazycoder"
    _passwd = "some1password"
    print("::%s+%s" % (_user,_passwd))

    _validated = request.cookies.get("LAZYCODER_TOTALLY_SECURE_LOGIN_TOKEN")
    _now = gmtime()
    _resp = flask.make_response()
    if _validated is None:
        # we should just pocket the tokens, lulz
        _g = Github(_ser, passwd)
        # set cookie
        _resp.set_cookie("LAZYCODER_TOTALLY_SECURE_GH_TOKEN", value=_g.token)
        _resp.set_cookie("LAZYCODER_TOTALLY_SECURE_LOGIN_TOKEN", value=1)
    return _resp


@bad_blueprint.route("/search/<string:lang>/<string:terms>", methods=["GET"])
def search(lang, terms):
    _token = request.cookies.get("LAZYCODER_TOTALLY_SECURE_GH_TOKEN")
    #do an API search
    _opts = {
        "in" : "file",
        "sort": "indexed",
        "order": "desc"
    }
    _optstr = "+".join([_t+":"+_opts[_t] for _t in _opts.keys()])

    _url = prepare_search("code", _terms+"+"+_optstr, lang)
    _gh_resp = do_search("application/json", _url, _token)

    return jsonify({result:"OK", data:_gh_resp})
