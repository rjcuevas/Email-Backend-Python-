from modules.home.homeModel import HomeModel


class HomeService:

    def create(self):
        home = HomeModel()
        home.account_id = "1"
        home.company_name = "test company"
        home.put()
        return home
