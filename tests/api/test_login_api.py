import requests

def test_login_api():
    url = "https://example-lms.com/api/login"
    data = {"username": "student", "password": "password"}
    res = requests.post(url, json=data)
    assert res.status_code == 200
    assert "token" in res.json()
