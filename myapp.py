import requests 
import json

# URL = "http://127.0.0.1:8000/stucreate/"

# data = {
#     'name' : 'Younis Ali',
#     'roll' : 3478,
#     'city' : 'karachi'
# }



# json_data = json.dumps(data)

# r = requests.post(url = URL , data = json_data)



# data = r.json()

# print(data)

URL = "http://127.0.0.1:8000/studentapi/"

# URL = 'http://127.0.0.1:8000/todo/'
def add_data():
    data = {
    'name' : 'buzar',
    'roll' : 546,
    'city' : 'lahore',
    }
    headers = {'content-Type'  :'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL , headers=headers , data= json_data)
    data = r.json()
    print(data)



# add_data()



def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id' : id}
    json_data = json.dumps(data)
    headers = {'content-Type'  :'application/json'}

    r = requests.get(url = URL, headers=headers , data = json_data)
    data = r.json()
    print(data) 



# get_data(3)    


def update_data():
    data = {
        'id' : 2,
        'city' : 'Kandhkot',
        # 'desc' : 'this is updated desc from the put method ',
        # 'is_done' : True
    }
    json_data = json.dumps(data)
    headers = {'content-Type'  :'application/json'}

    r = requests.put(url = URL , headers=headers, data = json_data)
    data = r.json()
    print(data)    



update_data()



def delete_data():
    data = { 'id' : 2 }
    json_data = json.dumps(data)
    r = requests.delete(url = URL , data = json_data)
    data = r.json()
    print(data)    



# delete_data()