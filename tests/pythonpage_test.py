"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/pythonPage.html")
    assert b"Python - Flask" in response.data
    assert response.status_code == 200
