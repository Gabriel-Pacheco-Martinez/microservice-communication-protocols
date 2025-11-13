# service-a/protocols/grpc_api.py
import grpc
from concurrent import futures
import time

from sqlalchemy.orm import Session
from models import User
from database import SessionLocal
from schemas import UserOut

from . import user_service_pb2
from . import user_service_pb2_grpc

# ====
# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ====
# Implement gRPC Service
class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    def GetUsers(self, request, context):
        db: Session = next(get_db())
        users = db.query(User).all()
        return user_service_pb2.UsersResponse(
            users=[user_service_pb2.User(id=u.id, name=u.name, email=u.email) for u in users]
        )

    def AddUser(self, request, context):
        db: Session = next(get_db())
        user = User(name=request.name, email=request.email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user_service_pb2.UserResponse(
            user=user_service_pb2.User(id=user.id, name=user.name, email=user.email)
        )

# ====
# Run gRPC server
def serve_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("✅ gRPC Service A running on port 50051")
    server.wait_for_termination()