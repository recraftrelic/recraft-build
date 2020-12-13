import requests
import json

from config import apiEndPoint, main_domain, headers


def add_a_sub_domain(domain_name):
    request = requests.post(apiEndPoint + "/domains/" + main_domain + "/records", headers=headers, data=json.dumps({
        "type": "CNAME",
        "name": domain_name,
        "data": main_domain + ".",
        "priority": None,
        "port": None,
        "ttl": 1800,
        "weight": None,
        "flags": None,
        "tag": None
    }))

    if request.status_code == 201:
        print("Added " + domain_name + " successfully")
    else:
        print(request.json()["message"])
