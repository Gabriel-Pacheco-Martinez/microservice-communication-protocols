# service-b/protocols/grpc_client.py
import grpc
from . import user_service_pb2
from . import user_service_pb2_grpc

class GRPCClientService:
    def __init__(self, host: str = "localhost", port: int = 50051):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = user_service_pb2_grpc.UserServiceStub(self.channel)

    def get_users(self):
        response = self.stub.GetUsers(user_service_pb2.Empty())
        return [{"id": u.id, "name": u.name, "email": u.email} for u in response.users]

    def add_user(self, payload):
        response = self.stub.AddUser(user_service_pb2.AddUserRequest(name=payload["name"], email=payload["email"]))
        u = response.user
        return {"id": u.id, "name": u.name, "email": u.email}