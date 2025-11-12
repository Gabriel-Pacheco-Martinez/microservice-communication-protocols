# service-a/protocols/graphql_api.py

import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List
from models import User
from database import SessionLocal
from schemas import UserOut

# ====
# DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ====
# Define GraphQL types (separate from Pydantic) -> Strawberry gets confused otherwise
@strawberry.type
class UserType:
    id: int
    name: str
    email: str

# ====
# GraphQL schema
@strawberry.type
class Query:
    @strawberry.field
    def get_users(self) -> List[UserType]:
        db = next(get_db())
        users = db.query(User).all()
        return [UserType(id=u.id, name=u.name, email=u.email) for u in users]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, name: str, email: str) -> UserType:
        db = next(get_db())
        user = User(name=name, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return UserType(id=user.id, name=user.name, email=user.email)

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)