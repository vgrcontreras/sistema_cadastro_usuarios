import pytest
from fastapi.testclient import TestClient

from cadastro_usuarios.main import app


@pytest.fixture
def client():
    return TestClient(app)
