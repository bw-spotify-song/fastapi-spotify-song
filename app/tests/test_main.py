"""
testing the root and predict path
"""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_docs():
    """Return HTML docs for root route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.headers['content-type'].startswith('text/html')


def test_predict():
    """Test the webs server response and the returned data type on predict method"""
    response = client.get('/predict/07j5RLJHwsm4cUb3GGoW3w')
    assert response.status_code == 200
    assert response.headers['content-type'].startswith('application/json')


if __name__ == '__main__':
    test_docs()
    test_predict()