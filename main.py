from modules.account.AccountController import AccountController
from modules.gcloud_samples.gcloud_samples_controller import GCloudSamplesController
from modules.home.homeController import HomeController
from modules.rest_api.restapicontroller import RestApiController
from google.appengine.api import urlfetch
from tg import TGController
from tg import expose


class MainController(TGController):

    home = HomeController()
    account = AccountController()
    gcloud_samples = GCloudSamplesController()
    api = RestApiController()

    @expose()
    def index(self):
        url = 'https://rjfront-dot-frontend-dot-cs-development-playground.appspot.com'

        try:
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                return result.content
            else:
                return result.status_code
        except urlfetch.Error:
            print "Caught exception fetching url"


        # go to http://localhost:8080, you should see this message
        #return "Welcome " + self.api.header()