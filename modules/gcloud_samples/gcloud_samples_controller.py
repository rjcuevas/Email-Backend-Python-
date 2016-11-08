from tg import TGController, expose


from modules.gcloud_samples.cloud_storage.cloud_storage_controller import CloudStorageController


class GCloudSamplesController(TGController):

    @expose()
    def index(self):
        return "gcloud samples"

    cloud_storage = CloudStorageController()