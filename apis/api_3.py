from flask import Flask, jsonify
import tracemalloc
import gc
import os
import logging
from objdict import ObjDict
import concurrent.futures
from flask_restplus import Namespace, Resource

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api = Namespace('Test3', description='Test 3')

def get_file_as_bytes(i):
    logger.debug(f'get_file_as_bytes {i} start')

    file = 'files/1.gri'
    with open(file, "rb") as fin:
        bytes = fin.read()

    logger.debug(f'get_file_as_bytes {i} end')
    return bytes

@api.route('/')
class Endpoint(Resource):
    """Test 3 thread"""

    @api.doc('Test 3')
    def get(self):
        number_of_files = 400
        result = []
        for i in range(0, number_of_files):
            file_stream = get_file_as_bytes(i)
            result.append(file_stream)

        count = len(result)
        return "OK"

