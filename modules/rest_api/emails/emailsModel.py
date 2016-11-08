from google.appengine.ext import ndb


class EmailMessageModel(ndb.Model):

    subject = ndb.StringProperty(indexed=True, required=True)
    body = ndb.TextProperty(indexed=True, required=False)
    recipients = ndb.TextProperty(repeated=True)
    sender = ndb.StringProperty(indexed=True, required=False)
    timestamp = ndb.DateTimeProperty()

    @classmethod  # if this will be removed error occur in order
    def query_emails_list(cls):
        return cls.query().order(-cls.subject)

    @staticmethod
    def deleteList(email):
        email_list = []
        for email_urlsafe in email:
            email_key = ndb.Key(urlsafe=email_urlsafe)
            email_list.append(email_key)
        ndb.delete_multi(email_list)


class EmailDraftModel(ndb.Model):
    subject = ndb.StringProperty(indexed=True, required=False)
    body = ndb.TextProperty(indexed=True, required=False)
    recipients = ndb.TextProperty(repeated=True)
    sender = ndb.StringProperty(indexed=True, required=False)
    timestamp = ndb.DateTimeProperty()

    # keyid = ndb.KeyProperty(kind='EmailsModel')

    @classmethod  # if this will be removed error occur in order
    def query_emails_list(cls):
        return cls.query().order(cls.subject)

    @staticmethod
    def deleteList(email):
        email_list = []
        for email_urlsafe in email:
            email_key = ndb.Key(urlsafe=email_urlsafe)
            email_list.append(email_key)
        ndb.delete_multi(email_list)

