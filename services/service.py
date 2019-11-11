import logging
import io
import os
import concurrent.futures
import bounded_pool_executor
#from xtgeo import RegularSurface, Surfaces

logger = logging.getLogger(__name__)


class Service:


    def __init__(self):

        logger.debug(f'Service Start')

    def get_files_as_streams(self, number_of_thread):
        streams = []

        for i in range(0, number_of_thread):
            file_stream = self.get_file_as_stream(i)
            streams.append(file_stream)

        return streams

    def get_files_as_streams_thread(self, number_of_thread):

        streams = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_thread) as executor:

            futures = {executor.submit(self.get_file_as_stream, i): i for i in range(0, number_of_thread)}
            i = 0
            for future in concurrent.futures.as_completed(futures):
                i = i + 1
                try:
                    file_stream = future.result()
                    del futures[future]
                    del future
                except Exception as exc:
                    logger.error(f'get_files_as_streams_thread {future}, generated an exception: {exc}')
                else:
                    streams.append(file_stream)
        return streams



    def get_files_as_bytes_thread(self, number_of_thread):

        bytes_list = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_thread) as executor:

            futures = {executor.submit(self.get_file_as_bytes, i): i for i in range(0, number_of_thread)}
            i = 0
            for future in concurrent.futures.as_completed(futures):
                i = i + 1
                try:
                    file_bytes = future.result()
                except Exception as exc:
                    logger.error(f'get_files_as_bytes_thread {future}, generated an exception: {exc}')
                else:
                    bytes_list.append(file_bytes)

            futures = None

        return bytes_list

    def get_files_as_bytes_thread_2(self, number_of_thread):
        bytes_list = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_thread) as executor:
            results = executor.map(self.get_file_as_bytes, range(0, number_of_thread))
            for result in results:
                bytes_list.append(result)

        return bytes_list

    def get_blob_streams_as_regularsurfaces_thread(self, blob_streams: list):

        surfs = []
        max_workers=os.cpu_count()
        with bounded_pool_executor.BoundedProcessPoolExecutor(max_workers=max_workers) as executor:

            futures = {executor.submit(self.get_RegularSurface, blob_stream): blob_stream for blob_stream in blob_streams}

            for future in concurrent.futures.as_completed(futures):
                try:
                    surf = future.result()
                except Exception as exc:
                    logger.error(f'get_streams_as_regularsurfaces: {future} generated an exception: {exc}')
                else:
                    surfs.append(surf)

        blob_streams = None
        futures = None
        return surfs

    def get_blob_streams_as_regularsurfaces(self, blob_streams: list):

        surfs = []

        for blob_stream in blob_streams:
            surfs.append(self.get_RegularSurface(blob_stream))

        blob_streams = None
        return surfs

    def get_blob_files_as_regularsurfaces(self, number_of_thread):

        logger.info(f'cpu_count: {os.cpu_count()}')

        with bounded_pool_executor.BoundedProcessPoolExecutor(os.cpu_count()) as process_executor:
            regular_surface_futures = {}

            with bounded_pool_executor.BoundedThreadPoolExecutor(max_workers=number_of_thread) as thread_executor:

                blob_to_stream_futures = {thread_executor.submit(self.get_file_as_stream, i): i for i in range(0, number_of_thread)}

                i = 0
                for future in concurrent.futures.as_completed(blob_to_stream_futures):
                    try:
                        i = i+1
                        file_stream = future.result()
                        del blob_to_stream_futures[future]
                        del future
                    except Exception as exc:
                        logger.error(f'get_blob_to_stream file_name {future}, generated an exception: {exc}')
                    else:
                        regular_surface_futures[process_executor.submit(self.get_RegularSurface, file_stream)] = i


            del blob_to_stream_futures
            surfs = []
            for future in concurrent.futures.as_completed(regular_surface_futures):
                try:
                    surf = future.result()
                    del regular_surface_futures[future]
                    del future
                except Exception as exc:
                    logger.error(f'RegularSurface: {future} generated an exception: {exc}')
                else:
                    surfs.append(surf)

            del regular_surface_futures
        return surfs



    def get_file_as_stream(self, i):
        logger.debug(f'get_file_as_stream {i} start')

        file = 'files/1.gri'
        with open(file, "rb") as fin:
            stream = io.BytesIO(fin.read())

        logger.debug(f'get_file_as_stream {i} end')
        return stream

    def get_RegularSurface(self, steam):
        logger.debug(f'get_test_strem')


        return "ok"

    def get_file_as_bytes(self, i):
        logger.debug(f'get_file_as_bytes {i} start')

        file = 'files/1.gri'
        with open(file, "rb") as fin:
            bytes = fin.read()

        logger.debug(f'get_file_as_bytes {i} end')
        return bytes

