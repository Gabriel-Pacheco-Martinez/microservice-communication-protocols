# General
from fastapi import FastAPI, Request, APIRouter
import time

# Mine
from protocols.rest_client import RESTClientService
from protocols.graphql_client import GraphQLClientService
from config import SERVICE_A_URL

# Prometheus Monitoring
from prometheus_fastapi_instrumentator import Instrumentator


# ====
# Server B
app = FastAPI()
router = APIRouter()

# ====
# Prometheus
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app) 

# ====
# Health check endpoint
@app.get("/ping")
def ping(request: Request):
    print(f"✅ Received /ping request from {request.client.host} at Service B")
    return {"status": "ok"}

# ====
@app.post("/request")
async def handle_request(request: Request):
    # Get information from artillery request
    body = await request.json()
    protocol = body.get("protocol")
    operation = body.get("operation")
    payload = body.get("payload")

    # Process request
    try:
        # ====
        # REST
        if protocol == "REST":
            client = RESTClientService(SERVICE_A_URL)
            if operation == "ping":
                client.ping_server()
            elif operation == "getUsers":
                users = client.get_users()
                print(f"✅ REST getUsers -> {users}")
                return {"users": users}
            elif operation == "addUser":
                users = client.add_user(payload)
                print(f"✅ REST addUser -> {user}")
                return {"user": user}
            else:
                return {"error": f"Unknown REST operation: {operation}"}
            
        # ====
        # GraphQL
        elif protocol == "GraphQL":
            client = GraphQLClientService(SERVICE_A_URL)
            if operation == "getUsers":
                users = client.get_users()
                print(f"✅ GraphQL getUsers -> {users}")
                return {"users": users}
            elif operation == "addUser":
                user = client.add_user(payload)
                print(f"✅ GraphQL addUser -> {user}")
                return {"user": user}
            else:
                return {"error": f"Unknown GraphQL operation: {operation}"}

        # ====
        # Unknown
        else:
            return {"error": f"Unknown protocol: {protocol}"}

    except Exception as e:
        print(f"❌ Error processing {protocol} request: {e}")

app.include_router(router)