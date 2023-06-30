import requests
from jsonschema.validators import validate
from helpers import load_json_schema
from usr_info import userdata, userdata2


def test_create_user():
    schema = load_json_schema('create_user.json')
    res = requests.post("https://petstore.swagger.io/v2/user", json=userdata)

    assert res.status_code == 200
    validate(instance=res.json(), schema=schema)


def test_update_user():
    schema = load_json_schema('update_user.json')
    res = requests.put(f"https://petstore.swagger.io/v2/user/{userdata2['username']}", json=userdata2)

    assert res.status_code == 200
    validate(instance=res.json(), schema=schema)


def test_user_login():
    schema = load_json_schema("user_login.json")
    res = requests.get(f"https://petstore.swagger.io/v2/user/login?username="
                       f"{userdata2['username']}"
                       f"&password={userdata2['password']}")

    validate(instance=res.json(), schema=schema)
    assert res.status_code == 200


def test_user_logout():
    schema = load_json_schema("user_logout.json")
    res = requests.get("https://petstore.swagger.io/v2/user/logout")

    validate(instance=res.json(), schema=schema)
    assert res.status_code == 200


def test_user_delete():
    schema = load_json_schema("user_delete.json")
    res = requests.delete(f"https://petstore.swagger.io/v2/user/{userdata2['username']}")

    validate(instance=res.json(), schema=schema)
    assert res.status_code == 200

#
#
# def test_create_array():
#     schema = load_json_schema('create_array.json')
#     res = requests.post('https://petstore.swagger.io/v2/user/createWithArray', json=[
#   {
#     "id": 0,
#     "username": "andry",
#     "firstName": "ecevev",
#     "lastName": "string",
#     "email": "string",
#     "password": "string",
#     "phone": "string",
#     "userStatus": 0
#   }
# ])
#     # print(res.text)
#     print(res.json())
#     validate(instance=res.json(), schema=schema)
#     assert res.status_code == 200
#
#
#
# def test_create_list():
#     schema = load_json_schema('create_list.json')
#     res = requests.post('https://petstore.swagger.io/v2/user/createWithList', json=[
#   {
#     "id": 0,
#     "username": "string",
#     "firstName": "string",
#     "lastName": "string",
#     "email": "string",
#     "password": "string",
#     "phone": "string",
#     "userStatus": 0
#   }
# ])
#     print(res.text)
#     validate(instance=res.json(), schema=schema)
#     assert res.status_code == 200
