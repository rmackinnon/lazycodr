import bad_idea_server
from bad_idea_server.github_search import do_search

from github import Github
from github.Authorization import Authorization

_g = Github("demo-lazycoder", "some1password")

print dir(Authorization.token)

