from flask import Flask, jsonify
#import tracemalloc
import gc
import os
import logging
from objdict import ObjDict
#import psutil
from services.service import Service

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from flask_restplus import Namespace, Resource

api = Namespace('Test1', description='Test 1')

service = Service()

#tracemalloc.start()

@api.route('/thread')
class Endpoint(Resource):
    """Test 1 thread"""

    @api.doc('Test 1')
    def get(self):
        number_of_files = 400

        result = service.get_files_as_streams_thread(number_of_files)
        #result = service.get_files_as_bytes_thread(number_of_files)
        l = len(result)
        result = None
        gc.collect()

        data = ObjDict()
        data.number_of_thread = l
        data.cpu_count = os.cpu_count()
        data.gc_get_count = list(gc.get_count())

        return jsonify(data)

@api.route('/nothread')
class Endpoint(Resource):
    """Test 1 no thread"""

    @api.doc('Test 1')
    def get(self):
        number_of_files = 400

        # service.get_files_as_streams_thread(number_of_thread)
        result = service.get_files_as_streams(number_of_files)
        l = len(result)
        result = None
        gc.collect()

        data = ObjDict()
        data.number_of_thread = l
        # data.virtual_memory = psutil.virtual_memory()
        data.cpu_count = os.cpu_count()
        # data.tracemalloc = tracemalloc.take_snapshot().traces._traces[:10]
        data.gc_get_count = list(gc.get_count())
        # data.gc_garbage = gc.garbage

        return jsonify(data)

