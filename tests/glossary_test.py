"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/glossary.html")
    assert b"Glossary" in response.data
    assert response.status_code == 200
