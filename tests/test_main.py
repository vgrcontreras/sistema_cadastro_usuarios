from http import HTTPStatus

from fastapi.testclient import TestClient

from cadastro_usuarios.main import app


def test_read_root_deve_retornar_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users',
        json={
            'first_name': 'teste_name',
            'last_name': 'teste_lastname',
            'password': 'teste_password',
            'email': 'teste@teste.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'first_name': 'teste_name',
        'last_name': 'teste_lastname',
        'email': 'teste@teste.com',
    }
