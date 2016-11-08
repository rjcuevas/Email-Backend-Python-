from modules.rest_api.emails.emailsService import EmailsService
from tg import TGController, expose, request
import json


class EmailsController(TGController):

    @expose()
    def index(self):
        return "EMAIL MODULE"

    @expose()
    def create(self):
        json_body = request.body
        data = json.loads(json_body)

        # creation of Emails entity in datastore service
        EmailsService().create_emails(data)
        return

    @expose('json')
    def list(self):
        list = EmailsService().get_emails()
        return list


    @expose('json')
    def delete(self):
        json_body = request.body
        data = json.loads(json_body)

        EmailsService().delete_emails(data)
        return

    @expose()
    def create_draft(self):
        json_body = request.body
        data = json.loads(json_body)

        # creation of Emails entity in datastore service
        EmailsService().create_emails_draft(data)
        return

    @expose('json')
    def list_draft(self):
        list = EmailsService().get_emails_draft()
        return list


    @expose('json')
    def delete_draft(self):
        json_body = request.body
        data = json.loads(json_body)

        EmailsService().delete_emails_draft(data)
        return