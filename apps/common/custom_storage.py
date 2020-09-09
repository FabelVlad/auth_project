from storages.backends.s3boto3 import S3Boto3Storage

from config import settings


class MediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = 'media'
