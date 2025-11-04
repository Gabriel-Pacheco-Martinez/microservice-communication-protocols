# General
import argparse

# Rest
from protocols.rest_client import RESTClientService
from config import SERVICE_A_URL

# ====
# REST client
def start_rest_client():
    print("\n" + "="*60)
    print("🔵 Testing REST Protocol")
    print("="*60)
    
    client = RESTClientService(SERVICE_A_URL)
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