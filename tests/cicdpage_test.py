"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/cicdPage.html")
    assert b"CI/CD" in response.data
    assert response.status_code == 200
