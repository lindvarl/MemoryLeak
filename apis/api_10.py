from flask import Flask, jsonify
import gc
import os
import logging
from objdict import ObjDict
from services.service import Service

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from flask_restplus import Namespace, Resource

api = Namespace('Test9', description='Test 9')

service = Service()


@api.route('/thread')
class Endpoint(Resource):
    """Test 10 thread"""

    @api.doc('Test 10')
    def get(self):
        number_of_files = 100

        bs = service.get_blobe_as_streams_thread(number_of_files)
        result = service.get_file_streams_as_regularsurfaces_thread(bs)
        l = len(result)
        del result
        del bs
        gc.collect()

        data = ObjDict()
        data.number_of_thread = l
        data.cpu_count = os.cpu_count()
        data.gc_get_count = list(gc.get_count())

        return jsonify(data)

@api.route('/nothread')
class Endpoint(Resource):
    """Test 10 no thread"""

    @api.doc('Test 10')
    def get(self):
        number_of_files = 100

        bs = service.get_blobe_as_streams(number_of_files)
        result = service.get_blob_streams_as_regularsurfaces(bs)

        l = len(result)
        del result
        del bs
        gc.collect()

        data = ObjDict()
        data.number_of_thread = l
        data.cpu_count = os.cpu_count()
        data.gc_get_count = list(gc.get_count())

        return jsonify(data)

