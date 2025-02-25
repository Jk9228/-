import requests

def send_to_server(method, name = '', id = '', interest = ''):
    url = 'http://127.0.0.1:8000/studentMethod/'
    
    myobj = {'Method': method, 'Name': name, 'ID':id, 'Interest':interest}
    
    headers = {'content-type': 'application/json'}
    
    x = requests.post(url, json=myobj, headers=headers)
    
    return x.text

# 測試發送請求
print(send_to_server('starify'))
