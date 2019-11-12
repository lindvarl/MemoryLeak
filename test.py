import requests
import time

def get_json(url):


    headers = {"Content-Type": "application/json"}
    s1 = time.time()
    response = requests.get(url, headers=headers)
    s2 = time.time()
    if response.status_code == 200:
        print(f'Time Used: {s2 - s1}')
        print(response.json())
    else:
        print(response.status_code)


if __name__ == '__main__':
    url = 'https://ml-api-ml-production.playground.radix.equinor.com/'
    #url = 'http://localhost:5000/'
    for i in range(0, 10):
        print(f'*************{i}******************')
        #print(get_json(url+'api/testok/'))
        #print(get_json(url+'api/test1/nothread'))
        #print(get_json(url+'api/test1/thread'))
        #print(get_json(url+'api/test2/nothread'))
        #print(get_json(url+'api/test2/thread'))
        #print(get_json(url+'api/test3/'))
        #print(get_json(url+'api/test4/nothread'))
        #print(get_json(url+'api/test4/thread'))
        #print(get_json(url+'api/test5/'))
        #print(get_json(url+'api/test6/nothread'))
        #print(get_json(url+'api/test6/thread'))
        #get_json(url+'api/test7/thread')
        #get_json(url + 'api/test8/thread')
        #get_json(url + 'api/test9/nothread') # OK
        get_json(url + 'api/test9/thread')
