from flask import Flask, jsonify
import gc
import os
import logging
from objdict import ObjDict
from services.service import Service

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from flask_restplus import Namespace, Resource

api = Namespace('Test8', description='Test 8')

service = Service()


@api.route('/thread')
class Endpoint(Resource):
    """Test 8 thread"""

    @api.doc('Test 8')
    def get(self):
        number_of_files = 100

        result = service.get_blob_files_as_regularsurfaces(number_of_files)

        l = len(result)
        del result
        gc.collect()

        data = ObjDict()
        data.number_of_thread = l
        data.cpu_count = os.cpu_count()
        data.gc_get_count = list(gc.get_count())

        return jsonify(data)

