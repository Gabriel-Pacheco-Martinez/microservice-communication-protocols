# General
import argparse


# ====
# SERVICE A: entry point
def main():
    # Arguments
    parser = argparse.ArgumentParser(
        description="Service A - Data Provider with Multiple Protocols"
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
    print(f"🔧 Service A Configuration")
    print(f"   Protocol: {args.protocol}")

    # Start the appropiate server based on protocol
    
    

if __name__ == "__main__":
    main()