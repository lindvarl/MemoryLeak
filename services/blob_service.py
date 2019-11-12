from azure.storage.blob import BlockBlobService
from azure.storage.blob.baseblobservice import BaseBlobService

import azure
import json
import os
import logging
from io import StringIO, BytesIO
import pandas as pd
import requests
import concurrent.futures
import bounded_pool_executor

logger = logging.getLogger(__name__)


class BlobService:
    """
        This class can be used for calling an Azure Blob Storage.

        Parameters
            account_name(str):
                Name of the Azure Storage account.
                Default value from environment variable DB_ACCOUNT_NAME.
            account_key(str):
                The Azure Storage account access key.
                Default value from environment variable DB_ACCOUNT_KEY.
    """

    def __init__(self, account_name=os.environ['DB_ACCOUNT_NAME'],
                 account_key= os.environ['DB_ACCOUNT_KEY'],):

        sess = requests.Session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
        sess.mount('https://', adapter)
        self.blob_service = BlockBlobService(account_name=account_name, account_key=account_key, request_session=sess)

        #self.blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
        self.account_name = account_name
        self.account_key = account_key

        logger.debug(f'blob_service.BlobService()')





    def get_blob_to_stream(self, i):
        """
            Call the blob storage and return BytesIO stream for given file name.

            Parameters
                container_name (string):Name of the Blob Container.
                file_name (string):Full path to one file in the blob container.
            Returns
                str:The BytesIO stream of the file.
        """
        try:
            container_name = 'johansverdrup'
            file_name = f'ens1/data/share/maps/depth/aasgard_fm_top--depth_surface--structural_model--realization-{i}.gri'

            logger.debug(f'get_blob_stream({file_name})')
            output_stream = BytesIO()
            self.blob_service.get_blob_to_stream(container_name, file_name, output_stream)
            return output_stream
        except azure.common.AzureMissingResourceHttpError as e:
            logger.error(f'Error code: {e.status_code}, Container Name: {container_name},  File Name: {file_name}')
            raise e



