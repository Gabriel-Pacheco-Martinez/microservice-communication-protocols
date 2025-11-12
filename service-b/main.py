# General
import argparse
import time
import threading
import uvicorn
import requests

# Rest
from protocols.rest_client import RESTClientService
from config import SERVICE_A_URL

# Server
from server import app

# ====
# Wait for Service A to be ready
def wait_for_service_a(url, retries=20, delay=2):
    for i in range(retries):
        try:
            resp = requests.get(f"{url}/api/ping", timeout=2)
            if resp.status_code == 200:
                print("✅ Service A is ready!")
                return True
        except Exception:
            print(f"Waiting for Service A... ({i+1}/{retries})")
            time.sleep(delay)
    raise Exception("❌ Service A did not start in time")

# ====
# Artillery listener
def start_service_b_server():
    config = uvicorn.Config(app, host="0.0.0.0", port=8080)
    server = uvicorn.Server(config)
    # server.serve()
    server.run()

# ====
# SERVICE B: entry point
def main():
    # Check Service A before starting Service B
    wait_for_service_a(SERVICE_A_URL)

    # Start Service B
    start_service_b_server()

if __name__ == "__main__":
    main()