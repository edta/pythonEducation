import requests


class TestApi:
    URL = "https://jsonplaceholder.typicode.com/"

    def test_get_posts(self):
        response = requests.get(self.URL + "posts")
        assert response.status_code == 200
        assert response.text != ""

    def test_get_first_post(self):
        response = requests.get(self.URL + "posts/1")
        assert response.status_code == 200
        assert response.json()['id'] == 1

    def test_invalid_route(self):
        response = requests.get(self.URL + "pasts")
        assert response.status_code == 404
