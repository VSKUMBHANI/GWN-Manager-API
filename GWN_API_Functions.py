#!/usr/bin/env python
import requests
import os
import json
from dotenv import load_dotenv
from hashlib import sha256
import time
from pprint import pprint


# Replace with your actual credentials
DEFAULT_ENV = "https://www.gwn.cloud" # Refer the URL: https://doc.grandstream.dev/GWN-API/EN/#api-160077149722401000249
ID_ENV = '116438' # Retrieved from the GDMS Cloud API Developer Portal.
SECRET_KEY_ENV = 'zs9nFH345DYER7WvCKMnenNheSyi2bsyk' # Retrieved from the GDMS Cloud API Developer Portal.

"""
Create a .env file in the same directory as the script and set the following environment variables:
    DEFAULT_URL: The base URL for the API.
    ID: Your client ID.
    Key: Your client secret.
 Then, you can load these variables using the dotenv library.
 Uncomment the following lines if you want to use environment variables.
"""
#load_dotenv()
#DEFAULT_ENV = os.getenv("DEFAULT_URL")
#ID_ENV = os.getenv("ID")
#SECRET_KEY_ENV = os.getenv("Key")

def get_token(DEFAULT_URL, ID, SECRET_KEY):
    Data = {
        "grant_type" : "client_credentials",
        "client_id" : ID,
        "client_secret" : SECRET_KEY
    }
    r = requests.get(DEFAULT_URL + "/oauth/token", params=Data)
    res = json.loads(r.text) 
    
    return res["access_token"]

def save_json_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_network(DEFAULT_URL, Access_token, appID, appSecret):
    timestamp = round(time.time() * 1000)
    public_params = {
        'access_token': Access_token,
        'appID': appID,
        'secretKey': appSecret,
        'timestamp': timestamp
    }
    body_data = {
        "type": "asc",
        "order": "id",
        "search": "",
        "pageNum": 1,
        "pageSize": 5
    }
    params = "&".join([f"{key}={public_params[key]}" for key in public_params])
    body = json.dumps(body_data, separators=(',', ':'))
    body_signature = sha256(body.encode()).hexdigest()
    signature = sha256(f"&{params}&{body_signature}&".encode()).hexdigest()
    payload_data = {
        'access_token': Access_token,
        'appID': appID,
        'timestamp': timestamp,
        'signature': signature
    }
    payload = "&".join([f"{key}={payload_data[key]}" for key in payload_data])
    network_url = f'{DEFAULT_URL}/oapi/v1.0.0/network/list'
    network_response = requests.get(network_url + "?" + payload, data=body, headers={'Content-type': 'application/json'}, timeout=30)
    data = ljson(network_response.text)['data']
    debug(data)
    save_json_to_file(data, "get_network.json")

def get_network_details(DEFAULT_URL, Access_token, appID, appSecret, networkID):
    timestamp = round(time.time() * 1000)
    public_params = {
        'access_token': Access_token,
        'appID': appID,
        'secretKey': appSecret,
        'timestamp': timestamp
    }
    body_data = {
        "id": networkID
    }
    params = "&".join([f"{key}={public_params[key]}" for key in public_params])
    body = json.dumps(body_data, separators=(',', ':'))
    body_signature = sha256(body.encode()).hexdigest()
    signature = sha256(f"&{params}&{body_signature}&".encode()).hexdigest()
    payload_data = {
        'access_token': Access_token,
        'appID': appID,
        'timestamp': timestamp,
        'signature': signature
    }
    payload = "&".join([f"{key}={payload_data[key]}" for key in payload_data])
    network_url = f'{DEFAULT_URL}/oapi/v1.0.0/network/detail'
    network_response = requests.post(network_url + "?" + payload, data=body, headers={'Content-type': 'application/json'}, timeout=30)
    data = ljson(network_response.text)['data']
    debug(data)
    save_json_to_file(data, "get_network_details.json")

def get_voucher(DEFAULT_URL, Access_token, appID, appSecret, networkID):
    timestamp = round(time.time() * 1000)
    public_params = {
        'access_token': Access_token,
        'appID': appID,
        'secretKey': appSecret,
        'timestamp': timestamp
    }
    body_data = {
        "search": "",
        "order": "name",
        "pageNum": 1,
        "pageSize": 10,
        "networkId": networkID
    }
    params = "&".join([f"{key}={public_params[key]}" for key in public_params])
    body = json.dumps(body_data, separators=(',', ':'))
    body_signature = sha256(body.encode()).hexdigest()
    signature = sha256(f"&{params}&{body_signature}&".encode()).hexdigest()
    payload_data = {
        'access_token': Access_token,
        'appID': appID,
        'timestamp': timestamp,
        'signature': signature
    }
    payload = "&".join([f"{key}={payload_data[key]}" for key in payload_data])
    network_url = f'{DEFAULT_URL}/oapi/v1.0.0/voucher/list'
    network_response = requests.post(network_url + "?" + payload, data=body, headers={'Content-type': 'application/json'}, timeout=30)
    data = ljson(network_response.text)['data']
    debug(data)
    save_json_to_file(data, "get_voucher.json")

def get_ssid(DEFAULT_URL, Access_token, appID, appSecret, networkID):
    timestamp = round(time.time() * 1000)
    public_params = {
        'access_token': Access_token,
        'appID': appID,
        'secretKey': appSecret,
        'timestamp': timestamp
    }
    body_data = {
        "search": "",
        "order": "name",
        "pageNum": 1,
        "pageSize": 10,
        "networkId": networkID
    }
    params = "&".join([f"{key}={public_params[key]}" for key in public_params])
    body = json.dumps(body_data, separators=(',', ':'))
    body_signature = sha256(body.encode()).hexdigest()
    signature = sha256(f"&{params}&{body_signature}&".encode()).hexdigest()
    payload_data = {
        'access_token': Access_token,
        'appID': appID,
        'timestamp': timestamp,
        'signature': signature
    }
    payload = "&".join([f"{key}={payload_data[key]}" for key in payload_data])
    network_url = f'{DEFAULT_URL}/oapi/v1.0.0/ssid/list'
    network_response = requests.post(network_url + "?" + payload, data=body, headers={'Content-type': 'application/json'}, timeout=30)
    data = ljson(network_response.text)['data']
    debug(data)
    save_json_to_file(data, "get_ssid.json")

def get_ap(DEFAULT_URL, Access_token, appID, appSecret, networkID):
    timestamp = round(time.time() * 1000)
    public_params = {
        'access_token': Access_token,
        'appID': appID,
        'secretKey': appSecret,
        'timestamp': timestamp
    }
    body_data = {
        "search": "",
        "order": "name",
        "pageNum": 1,
        "pageSize": 10,
        "networkId": networkID
    }
    params = "&".join([f"{key}={public_params[key]}" for key in public_params])
    body = json.dumps(body_data, separators=(',', ':'))
    body_signature = sha256(body.encode()).hexdigest()
    signature = sha256(f"&{params}&{body_signature}&".encode()).hexdigest()
    payload_data = {
        'access_token': Access_token,
        'appID': appID,
        'timestamp': timestamp,
        'signature': signature
    }
    payload = "&".join([f"{key}={payload_data[key]}" for key in payload_data])
    network_url = f'{DEFAULT_URL}/oapi/v1.0.0/ap/list'
    network_response = requests.post(network_url + "?" + payload, data=body, headers={'Content-type': 'application/json'}, timeout=30)
    data = ljson(network_response.text)['data']
    debug(data)
    save_json_to_file(data, "get_ap.json")

def get_portals(DEFAULT_URL, Access_token, appID, appSecret, networkID):
    timestamp = round(time.time() * 1000)
    public_params = {
        'access_token': Access_token,
        'appID': appID,
        'secretKey': appSecret,
        'timestamp': timestamp
    }
    body_data = {
        "networkId": networkID
    }
    params = "&".join([f"{key}={public_params[key]}" for key in public_params])
    body = json.dumps(body_data, separators=(',', ':'))
    body_signature = sha256(body.encode()).hexdigest()
    signature = sha256(f"&{params}&{body_signature}&".encode()).hexdigest()
    payload_data = {
        'access_token': Access_token,
        'appID': appID,
        'timestamp': timestamp,
        'signature': signature
    }
    payload = "&".join([f"{key}={payload_data[key]}" for key in payload_data])
    network_url = f'{DEFAULT_URL}/oapi/v1.0.0/portal/list'
    network_response = requests.post(network_url + "?" + payload, data=body, headers={'Content-type': 'application/json'}, timeout=30)
    data = ljson(network_response.text)['data']
    debug(data)
    save_json_to_file(data, "get_portals.json")

def get_device_details(DEFAULT_URL, Access_token, appID, appSecret, networkID, mac):
    timestamp = round(time.time() * 1000)
    public_params = {
        'access_token': Access_token,
        'appID': appID,
        'secretKey': appSecret,
        'timestamp': timestamp
    }
    body_data = {
        "mac": mac,
        "networkId": networkID
    }
    params = "&".join([f"{key}={public_params[key]}" for key in public_params])
    body = json.dumps(body_data, separators=(',', ':'))
    body_signature = sha256(body.encode()).hexdigest()
    signature = sha256(f"&{params}&{body_signature}&".encode()).hexdigest()
    payload_data = {
        'access_token': Access_token,
        'appID': appID,
        'timestamp': timestamp,
        'signature': signature
    }
    payload = "&".join([f"{key}={payload_data[key]}" for key in payload_data])
    network_url = f'{DEFAULT_URL}/oapi/v1.0.0/device/info'
    network_response = requests.post(network_url + "?" + payload, data=body, headers={'Content-type': 'application/json'}, timeout=30)
    data = ljson(network_response.text)['data']
    debug(data)
    save_json_to_file(data, "get_device_details.json")

def get_inventory(DEFAULT_URL, Access_token, appID, appSecret, networkID):
    timestamp = round(time.time() * 1000)
    public_params = {
        'access_token': Access_token,
        'appID': appID,
        'secretKey': appSecret,
        'timestamp': timestamp
    }
    body_data = {
        "networkId": networkID
    }
    params = "&".join([f"{key}={public_params[key]}" for key in public_params])
    body = json.dumps(body_data, separators=(',', ':'))
    body_signature = sha256(body.encode()).hexdigest()
    signature = sha256(f"&{params}&{body_signature}&".encode()).hexdigest()
    payload_data = {
        'access_token': Access_token,
        'appID': appID,
        'timestamp': timestamp,
        'signature': signature
    }
    payload = "&".join([f"{key}={payload_data[key]}" for key in payload_data])
    network_url = f'{DEFAULT_URL}/oapi/v1.0.0/inventory/list'
    network_response = requests.post(network_url + "?" + payload, data=body, headers={'Content-type': 'application/json'}, timeout=30)
    data = ljson(network_response.text)['data']
    debug(data)
    save_json_to_file(data, "get_inventory.json")

def ljson(input):
    json_return = json.loads(str(input))
    return json_return


def debug(input):
    pprint(input)
    print("")

key = get_token(DEFAULT_URL=DEFAULT_ENV, ID=ID_ENV, SECRET_KEY=SECRET_KEY_ENV)
print("Network:")
get_network(DEFAULT_URL=DEFAULT_ENV, Access_token=key, appID=ID_ENV, appSecret=SECRET_KEY_ENV)
print("Network Details:")
get_network_details(DEFAULT_URL=DEFAULT_ENV, Access_token=key, appID=ID_ENV, appSecret=SECRET_KEY_ENV, networkID=83802) #Use get_network() to get the networkID.
print("Voucher:")
get_voucher(DEFAULT_URL=DEFAULT_ENV, Access_token=key, appID=ID_ENV, appSecret=SECRET_KEY_ENV, networkID=83802) #Use get_network() to get the networkID.
print("SSID:")
get_ssid(DEFAULT_URL=DEFAULT_ENV, Access_token=key, appID=ID_ENV, appSecret=SECRET_KEY_ENV, networkID=83802) #Use get_network() to get the networkID.
print("APs:")
get_ap(DEFAULT_URL=DEFAULT_ENV, Access_token=key, appID=ID_ENV, appSecret=SECRET_KEY_ENV, networkID=83802) #Use get_network() to get the networkID.
print("Portal:")
get_portals(Access_token=key, appID=ID_ENV, appSecret=SECRET_KEY_ENV, DEFAULT_URL=DEFAULT_ENV, networkID=83802) #Use get_network() to get the networkID.
print("Device Details:")
get_device_details(Access_token=key, appID=ID_ENV, appSecret=SECRET_KEY_ENV, DEFAULT_URL=DEFAULT_ENV, networkID=83802, mac="C0:74:AD:F9:83:DC") #Use get_network() to get the networkID.
print("Inventory:")
get_inventory(Access_token=key, appID=ID_ENV, appSecret=SECRET_KEY_ENV, DEFAULT_URL=DEFAULT_ENV, networkID=83802) #Use get_network() to get the networkID.
