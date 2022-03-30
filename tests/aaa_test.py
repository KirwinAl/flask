"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/aaatesting.html")
    assert b"AAA Testing" in response.data
    assert response.status_code == 200
