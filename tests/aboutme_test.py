"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/aboutme.html")
    assert b"About Me" in response.data
    assert response.status_code == 200
