import requests
import pytest


class TestRestApi:
    URL = "https://jsonplaceholder.typicode.com/"

    @pytest.mark.parametrize(
        "url_path, response_status_code", [
            ("posts/", 200),
            ("pasts/", 404),
            ("posts/1/", 200),
            ("posts/100/", 200),
            ("posts/0/", 404),
            ("posts/101/", 404)
       ]
    )
    def test_get(self, url_path, response_status_code):
        response = requests.get(self.URL + url_path)
        assert response.status_code == response_status_code

    @pytest.mark.parametrize(
        "title, body, userId, response_status_code", [
            ('post_example', 'body_example', 101, 201),
            (None, None, None, 201),
        ]
    )
    def test_post(self, title, body, userId, response_status_code):
        response = requests.post(self.URL + "posts", json={
            "title": title,
            "body": body,
            "userId": userId})
        assert response.status_code == response_status_code

    @pytest.mark.parametrize(
        "id, title, body, userId, response_status_code", [
            (1, 'post_example', 'body_example', 1, 200),
            (None, None, None, None, 200)
        ]
    )
    def test_put(self, id,  title, body, userId, response_status_code):
        response = requests.put(self.URL + "posts/1", json={
            'id': id,
            "title": title,
            "body": body,
            "userId": userId})
        assert response.status_code == response_status_code

    @pytest.mark.parametrize(
        "id, response_status_code", [
            (1, 200),
            (0, 200),
            (-1, 200),
            (99, 200),
            (100, 200),
            (101, 200)
        ]
    )
    def test_delete(self, id, response_status_code):
        response = requests.delete(self.URL + f"posts/{id}")
        assert response.status_code == response_status_code