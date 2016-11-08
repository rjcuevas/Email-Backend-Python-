from modules.rest_api.emails.emailsModel import EmailMessageModel
from modules.rest_api.emails.emailsModel import EmailDraftModel
from google.appengine.api import users
import datetime

class EmailsService:

    def create_emails(self, email):
        user = users.get_current_user()
        emails = EmailMessageModel()
        emails.subject = email.get("subject")
        emails.body = email.get("body")
        emails.recipients = email.get("recipients")
        emails.sender = user.email()
        emails.timestamp = datetime.datetime.now()
        emails.put()

    def get_emails(self):
        emails = EmailMessageModel()
        list = emails.query_emails_list()
        emails = []
        for email in list:
            emails.append({"urlsafe": email.key.urlsafe(), "subject": email.subject, "body": email.body, "recipients": email.recipients, "sender": email.sender, "timestamp": email.timestamp})
        data = dict(data=emails)
        return data

    def delete_emails(self, email):
        emails = EmailMessageModel()
        emails.deleteList(email)

    def create_emails_draft(self, email):
        user = users.get_current_user()
        emails = EmailDraftModel()
        emails.subject = email.get("subject")
        emails.body = email.get("body")
        emails.recipients = email.get("recipients")
        emails.sender = user.email()
        emails.timestamp = datetime.datetime.now()
        emails.put()

    def get_emails_draft(self):
        emails = EmailDraftModel()
        list = emails.query_emails_list()
        emails = []
        for email in list:
            emails.append({"urlsafe": email.key.urlsafe(), "subject": email.subject, "body": email.body, "recipients": email.recipients, "sender": email.sender, "timestamp": email.timestamp})
        data = dict(data=emails)
        return data

    def delete_emails_draft(self, email):
        emails = EmailDraftModel()
        emails.deleteList(email)
