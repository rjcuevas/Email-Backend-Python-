import os
import SimpleHTTPServer

from tg import TGController, expose
from google.appengine.api import users


class UserController(TGController):

    @expose()
    def index(self):
        return "USER MODULE"

    @expose('json')
    def auth(self):
        user = users.get_current_user()
        value = {}
        if not user:
            value = {
                "login_url": users.create_login_url('/')
                     }
        else:
            value = {
                "user_email" : user.email(),
                "nickname" : user.nickname()
                     }
        return value

    @expose('json')
    def logout(self):
        value =  {
                "logout_url": users.create_logout_url('/')
            }
        return value
