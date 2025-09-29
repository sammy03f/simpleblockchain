import hashlib 
import time    
import json 

class Block:  
    def __init__(self, index, data, previous_hash):
        # Position of the block in the blockchain
        self.index = index
        # Time when the block is created (in seconds since epoch)
        self.timestamp = time.time()
        # The actual data or transactions stored in the block
        self.data = data
        # Hash of the previous block in the chain
        self.previous_hash = previous_hash
        # Number used for mining 
        self.nonce = 0
        # The hash of the current block, calculated using its contents
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        
        # Serialize the block's contents into a JSON string
        block_string = json.dumps({
            "index": self.index,           
            "timestamp": self.timestamp,   
            "data": self.data,            
            "previous_hash": self.previous_hash, 
            "nonce": self.nonce         
        }, sort_keys=True)
        # Calculate SHA-256 hash, return its hexadecimal representation
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty):
    
        # String of '0's that the hash must start with, based on difficulty
        target = "0" * difficulty
        # Loop until the block's hash starts with the required number of '0's
        while self.hash[:difficulty] != target:
            # Increment nonce to change the hash
            self.nonce += 1
            # Recalculate the hash with the new nonce
            self.hash = self.calculate_hash()
        # Print the mined block's hash
        print(f"Block mined! Hash: {self.hash}")
        # Return the final hash
        return self.hash
    
    def __str__(self):
        # Return a string representation of the block, showing index, hash, and data
        return f"Block #{self.index} - Hash: {self.hash[:10]}... - Data: {self.data}"
