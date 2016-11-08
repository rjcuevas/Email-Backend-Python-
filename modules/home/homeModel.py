from google.appengine.ext import ndb


class HomeModel(ndb.Model):

    account_id = ndb.StringProperty(indexed=True, required=True)
    company_name = ndb.StringProperty(indexed=True, required=False)
    person_name = ndb.StringProperty(indexed=True, required=False)
    phone_number = ndb.StringProperty(indexed=True, required=False)
    address = ndb.StringProperty(indexed=False, required=False)
    special_requirements = ndb.TextProperty(indexed=False, required=False)
    remarks = ndb.TextProperty(indexed=False, required=False)