import requests

def get_json(url):


    headers = {"Content-Type": "application/json"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.status_code


if __name__ == '__main__':
    for i in range(0, 500):
        print(f'*************{i}******************')
        #print(get_json('http://localhost:5000/api/testok/'))
        #print(get_json('http://localhost:5000/api/test1/nothread'))
        #print(get_json('http://localhost:5000/api/test1/thread'))
        #print(get_json('http://localhost:5000/api/test2/nothread'))
        #print(get_json('http://localhost:5000/api/test2/thread'))
        #print(get_json('http://localhost:5000/api/test3/'))
        #print(get_json('http://localhost:5000/api/test4/nothread'))
        #print(get_json('http://localhost:5000/api/test4/thread'))
        #print(get_json('http://localhost:5000/api/test5/'))
        #print(get_json('http://localhost:5000/api/test6/nothread'))
        #print(get_json('http://localhost:5000/api/test6/thread'))
        print(get_json('http://localhost:5000/api/test7/thread'))