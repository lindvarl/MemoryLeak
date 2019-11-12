from flask import Flask, jsonify
#import tracemalloc
import gc
import os
import logging
from objdict import ObjDict
import concurrent.futures
from flask_restplus import Namespace, Resource

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api = Namespace('Test2', description='Test 2')

#tracemalloc.start()

#"gc.set_debug(gc.DEBUG_SAVEALL)


def get_file_as_bytes(i):
    logger.debug(f'get_file_as_bytes {i} start')

    file = './files/1.gri'
    with open(file, "rb") as fin:
        bytes = fin.read()

    logger.debug(f'get_file_as_bytes {i} end')
    return bytes

@api.route('/thread')
class Endpoint(Resource):
        """Test 1 thread"""

        @api.doc('Test 1')
        def get(self):
            number_of_files = 400
            gc.collect()
            #snapshot1 = tracemalloc.take_snapshot()

            result = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_files) as executor:

                futures = {executor.submit(get_file_as_bytes, i): i for i in range(0, number_of_files)}
                i = 0
                for future in concurrent.futures.as_completed(futures):
                    i = i + 1
                    try:
                        file_bytes = future.result()
                    except Exception as exc:
                        logger.error(f'get_files_as_bytes_thread {future}, generated an exception: {exc}')
                    else:
                        result.append(file_bytes)

                #futures = None

            count = len(result)
            result = None
            gc.collect()

            data = ObjDict()
            data.number_of_thread = count
            # data.virtual_memory = psutil.virtual_memory()
            data.cpu_count = os.cpu_count()
            # data.tracemalloc = tracemalloc.take_snapshot().traces._traces[:10]
            data.gc_get_count = list(gc.get_count())
            # data.gc_garbage = gc.garbage

            #snapshot2 = tracemalloc.take_snapshot()
            #top_stats = snapshot2.compare_to(snapshot1, 'lineno')

            top_stats_list = []
            print("[ Top 10 ]")
            data.top_stats = top_stats_list
            return jsonify(data)


@api.route('/nothread')
class Endpoint(Resource):
    """Test 1 no thread"""

    @api.doc('Test 4')
    def get(self):
        number_of_files = 400
        gc.collect()
        #snapshot1 = tracemalloc.take_snapshot()


        result = []
        for i in range(0, number_of_files):
            file_stream = get_file_as_bytes(i)
            result.append(file_stream)

        count = len(result)
        result = None
        gc.collect()

        data = ObjDict()
        data.number_of_thread = count
        # data.virtual_memory = psutil.virtual_memory()
        data.cpu_count = os.cpu_count()
        # data.tracemalloc = tracemalloc.take_snapshot().traces._traces[:10]
        data.gc_get_count = list(gc.get_count())
        # data.gc_garbage = gc.garbage

        #snapshot2 = tracemalloc.take_snapshot()
        #top_stats = snapshot2.compare_to(snapshot1, 'lineno')

        top_stats_list = []
        print("[ Top 10 ]")
        data.top_stats = top_stats_list
        return jsonify(data)


