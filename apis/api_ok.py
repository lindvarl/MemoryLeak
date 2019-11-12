from flask_restplus import Namespace, Resource

api = Namespace('TestOk', description='Test Ok')

@api.route('/')
class Endpoint(Resource):
    """Test Ok"""

    @api.doc('Test Ok')
    def get(self):
        """get Test Ok"""
        number_of_files = 400

        result = []
        for i in range(0, number_of_files):
            file = './files/1.gri'
            with open(file, "rb") as fin:
                result.append(fin.read())

        return "OK"

