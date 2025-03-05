import requests

def test_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200

def test_response_content():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    assert len(data) > 0
