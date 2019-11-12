from flask_restplus import Api
from .api_ok import api as ok
from .api_1 import api as a1
from .api_2 import api as a2
from .api_3 import api as a3
from .api_4 import api as a4
from .api_5 import api as a5
from .api_6 import api as a6
from .api_7 import api as a7
from .api_8 import api as a8
from .api_9 import api as a9
from .api_10 import api as a10

api = Api()
api.add_namespace(ok, path='/api/testok')
api.add_namespace(a1, path='/api/test1')
api.add_namespace(a2, path='/api/test2')
api.add_namespace(a3, path='/api/test3')
api.add_namespace(a4, path='/api/test4')
api.add_namespace(a5, path='/api/test5')
api.add_namespace(a6, path='/api/test6')
api.add_namespace(a7, path='/api/test7')
api.add_namespace(a8, path='/api/test8')
api.add_namespace(a9, path='/api/test9')
api.add_namespace(a10, path='/api/test10')