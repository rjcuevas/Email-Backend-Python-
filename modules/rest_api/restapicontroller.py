from google.appengine.api import users
from modules.rest_api.emails.emailsController import EmailsController
from modules.rest_api.user.userController import UserController
from tg import TGController, expose

class RestApiController(TGController):

    user = UserController()
    emails = EmailsController()

    @expose()
    def index(self):
        return "API MODULE"

    def header(self):
        user = users.get_current_user()
        nickname = user.nickname()
        logout_url = users.create_logout_url('/')
        head = '{} (<a href="{}">sign out</a>) </br>'.format(nickname, logout_url)
        return head