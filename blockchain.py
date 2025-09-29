from block import Block
import hashlib

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty
        self.pending_transactions = []
        
        # Create the genesis block
        self.create_genesis_block()
    
    def create_genesis_block(self):
        """Create the first block in the chain"""
        genesis_block = Block(0, "Genesis Block", "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
        print("Genesis block created!")
    
    def get_latest_block(self):
        """Get the most recent block in the chain"""
        return self.chain[-1]
    
    def add_block(self, data):
    
        previous_block = self.get_latest_block()
        new_block = Block(previous_block.index + 1, data, previous_block.hash)
        
        # Mine the block
        new_block.mine_block(self.difficulty)
        
        # Add to chain
        self.chain.append(new_block)
        print(f"New block added: {new_block}")
    
    def is_chain_valid(self):
        
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check if current block hash is correct
            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash in block {i}")
                return False
            
            # Check if previous hash matches
            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid previous hash in block {i}")
                return False
        
        return True
    
    def get_chain_info(self):
        
        print(f"\n=== Blockchain Info ===")
        print(f"Number of blocks: {len(self.chain)}")
        print(f"Mining difficulty: {self.difficulty}")
        print(f"Chain valid: {self.is_chain_valid()}")
        print("=======================\n")
    
    def display_chain(self):
        """Display all blocks in the chain"""
        print("\n=== Blockchain ===")
        for block in self.chain:
            print(block)
        print("==================\n")
