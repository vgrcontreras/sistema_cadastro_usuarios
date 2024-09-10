from http import HTTPStatus

from fastapi import FastAPI

from cadastro_usuarios.schemas import UserSchema, UserSchemaPublic

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Hello World'}


@app.post(
    '/users',
    status_code=HTTPStatus.CREATED,
    response_model=UserSchemaPublic,
)
def create_user(user: UserSchema):
    return user
