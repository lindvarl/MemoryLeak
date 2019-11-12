import requests

def get_json(url):


    headers = {"Content-Type": "application/json"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.status_code


if __name__ == '__main__':
    #url = 'https://ml-api-ml-production.playground.radix.equinor.com/'
    url = 'http://localhost:5000/'
    for i in range(0, 20):
        print(f'*************{i}******************')
        print(get_json(url+'api/testok/'))
        print(get_json(url+'api/test1/nothread'))
        print(get_json(url+'api/test1/thread'))
        print(get_json(url+'api/test2/nothread'))
        print(get_json(url+'api/test2/thread'))
        print(get_json(url+'api/test3/'))
        print(get_json(url+'api/test4/nothread'))
        print(get_json(url+'api/test4/thread'))
        print(get_json(url+'api/test5/'))
        print(get_json(url+'api/test6/nothread'))
        print(get_json(url+'api/test6/thread'))
        print(get_json(url+'api/test7/thread'))