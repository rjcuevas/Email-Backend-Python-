# fix imports for appengine environmentsimport sys
import os
import fix_imports
(fix_imports)

from tg import AppConfig
from tg import redirect, response
from google.appengine.api import users
from main import MainController


def controller_wrapper(next_caller):
    def call(*args, **kw):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Access-Control-Allow-Origin, Authorization, X-Requested-With'
        user = users.get_current_user()
        path = os.environ['PATH_INFO']
        if not user:
            if "api/user/auth" not in path:
            #if "api/user/auth" not in path and "api/emails/create" not in path:
                login_url = users.create_login_url('/')
                redirect(login_url)

        return next_caller(*args, **kw)

    return call

config = AppConfig(minimal=True, root_controller=MainController())
config.register_controller_wrapper(controller_wrapper)
app = config.make_wsgi_app()

