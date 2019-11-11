from flask_restplus import Namespace, Resource

api = Namespace('Test5', description='Test 5')

def get_file_as_bytes(i):

    file = 'files/1.gri'
    with open(file, "rb") as fin:
        bytes = fin.read()

    return bytes

@api.route('/')
class Endpoint(Resource):
    """Test 5"""

    @api.doc('Test 5')
    def get(self):
        """get Test 5"""
        number_of_files = 400

        result = []
        for i in range(0, number_of_files):
            result.append(get_file_as_bytes(i))

        return "Test 5"

