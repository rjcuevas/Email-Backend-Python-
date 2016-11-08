from tg import TGController
from tg import expose
from google.cloud import storage


class CloudStorageController(TGController):

    @expose()
    def index(self):
        client = storage.Client()
        bucket = client.get_bucket('<your-bucket-name>')
        blob = bucket.blob('my-test-file.txt')
        blob.upload_from_string('this is test content!')