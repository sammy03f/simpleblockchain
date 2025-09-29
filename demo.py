from blockchain import Blockchain
import time

def main():
    print("Creating a simple blockchain...")
    
    # Create a new blockchain with difficulty 2 (means hash must start with "00")
    blockchain = Blockchain(difficulty=2)
    
    # Add some blocks with sample data
    print("\n Adding some blocks...")
    
    blockchain.add_block("Alice sends 10 coins to Bob")
    time.sleep(1)  # Small delay to see different timestamps
    
    blockchain.add_block("Bob sends 5 coins to Charlie")
    time.sleep(1)
    
    blockchain.add_block("Charlie sends 3 coins to David")
    
    blockchain.display_chain()
    

    blockchain.get_chain_info()
    
    # Demonstrate validation
    print(" Validating the blockchain...")
    if blockchain.is_chain_valid():
        print(" Blockchain is valid!")
    else:
        print(" Blockchain is invalid!")
    
    print("\n Demo completed! You now have a working blockchain!")

if __name__ == "__main__":
    main()
