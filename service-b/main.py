# General
import argparse
import time

# Rest
from protocols.rest_client import RESTClientService
from config import SERVICE_A_URL

# ====
# Check if server is alive
def is_server_alive(client, retries=20, delay=2):
    for i in range(retries):
        try:
            resp = client.ping_server()
            if resp.get("db_connection") == "ok":
                print("✅ Service A is ready!")
                return
        except Exception as e:
            print(f"Waiting for Service A... ({i+1}/{retries})")
            time.sleep(delay)
    raise Exception("❌ Service A did not start in time")

# ====
# REST client
def start_rest_client():
    client = RESTClientService(SERVICE_A_URL)
    is_server_alive(client)
    users = client.get_users()
    print(f"✅ Found {len(users)} users")
    for user in users:
        print(f"   - {user['name']} ({user['email']})")

# ====
# SERVICE B: entry point
def main():
    parser = argparse.ArgumentParser(
        description="Service B - Data Consumer with Multiple Protocol Clients"
    )
    parser.add_argument(
        "--protocol",
        type=str,
        choices=["REST", "gRPC", "GraphQL"],
        default="REST",
        help="Communication protocol to use (default: REST)"
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print(f"🔧 Service B Configuration")
    print(f"   Protocol: {args.protocol}")
    
    # Run the appropriate client test
    if args.protocol == "REST":
        start_rest_client()

if __name__ == "__main__":
    main()