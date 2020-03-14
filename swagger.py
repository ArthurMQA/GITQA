import requests
import json
'''
Swagger API call v 0.5
'''

base_url = 'https://petstore.swagger.io/v2'


def pet(petid):
    api_url = f"{base_url}/pet/{petid}"
    r = requests.get(api_url)
    return r

def pet_find(status):
    api_url = f"{base_url}/pet/findByStatus?status={status}"
    r = requests.get(api_url)
    return r

def pet_del(petid):
    api_url = f"{base_url}/pet/{petid}"
    r = requests.delete(api_url)
    return r

def pet_upd(petid, name, status="available"):
    api_url = f"{base_url}/pet/{petid}"
    api_data = {
        'petId':petid,
        'name':name,
        'status':status
        }
    r = requests.post(api_url, api_data)
    return r    

def req_info(r):
    try:
        answer = r.json()
    except json.decoder.JSONDecodeError:
        answer = r.content
    print("Status Code:",r.status_code)
    print(answer)

if __name__ == '__main__':
    r = pet(1)
    req_info(r)
    r = pet(0)
    req_info(r)
    r = pet(5.01)
    req_info(r)

    print("UPD")
    r = pet_upd(1, "dog")
    req_info(r)