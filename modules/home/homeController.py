from tg import TGController, expose

from modules.home.homeService import HomeService
from tg.controllers.util import redirect
#from google.appengine.api import users

class HomeController(TGController):

    @expose()
    def index(self):
        redirect("home/list")

    @expose()
    def create(self):
        # creation of home entity in datastore service
        data = HomeService().create()
        return data.key.urlsafe()

    @expose()
    def edit(self):
        return "home edit page"

    @expose()
    def delete(self):
        return "home edit page"

    @expose()
    def list(self):
        return "home list page"

    """def greetings(self):
        user = users.get_current_user()
        nickname = user.nickname()
        logout_url = users.create_logout_url('/')
        greeting = 'Welcome, {}! (<a href="{}">sign out</a>) </br>'.format(nickname, logout_url)
        return greeting"""