from rest_framework.response import Response
from datetime import datetime

class CheckTime():

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print('Hello')
        start = datetime.now()
        response: Response = self.get_response(request)
        end = datetime.now()
        print('total time', end - start)
        # print(type(response))
        # print(response.data)
        # order_dict = response.data['test'] = 'test'
        # print(response.data)
        return response