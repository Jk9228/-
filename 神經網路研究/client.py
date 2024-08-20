import requests

def send_to_server(name):
    url = 'http://127.0.0.1:8000/receive_Data/'
    
    myobj = {'name':name}
    
    headers = {'content-type': 'application/json'}
    x = requests.post(url, json = myobj, headers=headers)
    
    return x.text