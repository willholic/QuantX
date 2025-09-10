from solana.rpc.api import Client

def main():
    # Connect to the Solana mainnet cluster
    client = Client("https://api.mainnet-beta.solana.com")

    # Check if the client is connected
    if client.is_connected():
        print("Connected to Solana mainnet beta")
        # Get the latest blockhash
        latest_blockhash = client.get_latest_blockhash()
        print(f"Latest blockhash: {latest_blockhash}")
    else:
        print("Failed to connect to Solana mainnet beta")

if __name__ == "__main__":
    main()
