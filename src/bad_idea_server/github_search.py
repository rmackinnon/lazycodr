__name__ = "bad_idea_server.github_search"
__package__ = "bad_idea_server"

from urllib import urlencode
from urllib2 import Request, urlopen

"""
Source: https://developer.github.com/v3/search/
"""

GH_URI = "https://api.github.com/search"
GH_MEDIATYPE = "application/vnd.github.mercy-preview+json"
GH_COMMIT = "application/vnd.github.cloak-preview"

"""
created or pushed: Filters repositories based on date of creation, or when they were last updated.

fork: Filters whether forked repositories should be included (true) or only forked repositories should be returned (only).

forks: Filters repositories based on the number of forks.
in Qualifies which fields are searched. With this qualifier you can restrict the search to just the repository name, description, readme, or any combination of these.

language: Searches repositories based on the language they're written in.

license: Filters repositories by license or license family, using the license keyword.

repo or user: Limits searches to a specific repository or user.

size: Finds repositories that match a certain size (in kilobytes).

stars: Searches repositories based on the number of stars.

topic: Filters repositories based on the specified topic.

archived: Filters whether archived repositories should be included (true) or not (false)
"""
Q_TYPES = [
     "pushed",
     "created",
     "fork",
     "forks",
     "language",
     "license",
     "repo",
     "user",
     "size",
     "stars",
     "topic",
     "archived"
]

GET_PARAMS = ["q", "sort", "order"]


def do_auth(user, passwd, token):
    # We need something here for auth DO THIS
    return token


def prepare_search(sType, terms, language, order="desc"):
    _url = GH_URI + '/' + sType
    _values = { "q": terms, "sort": "indexed", "ordered": order}
    _language = "language:"+language
    _options = urlencode()

    return _url


def do_search(media, url, token):
    # Standup connection
    _header = {"Accept" : media, "Authorization" : token}
    # open request
    try:
        _req = Request(headers=_header, url=url)
        _response = _req.urlopen(_req)
    except Exception as e:
        return {"error": str(e)}
    # read result
    return {"response": _response.json()}
