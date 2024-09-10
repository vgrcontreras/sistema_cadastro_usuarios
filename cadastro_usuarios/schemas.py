from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    first_name: str
    last_name: str
    password: str
    email: EmailStr

class UserSchemaPublic(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr

