# This file initializes the configurations for tests
import pytest

from src.routes import api as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()