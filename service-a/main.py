# main.py
import uvicorn
import threading
from fastapi import FastAPI
from protocols.rest_api import rest_router
from protocols.graphql_api import graphql_app
from protocols.grpc_api import serve_grpc

# ====
# Create unified FastAPI app
app = FastAPI(
    title="Service A",
    description="Single entry point for Service A supporting protocol APIs.",
    version="1.0.0"
)

# Include both protocols
app.include_router(rest_router, prefix="/api")
app.include_router(graphql_app, prefix="/graphql")

# ====
# Events
@app.on_event("startup")
def startup_event():
    print("✅ Unified Service A running on:")
    print("   - REST:     http://0.0.0.0:8000/api")
    print("   - GraphQL:  http://0.0.0.0:8000/graphql")
    print("   - gRPC:     port 50051")

    # Start gRPC server in background thread
    threading.Thread(target=serve_grpc, daemon=True).start()

# ====
# Main
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)