import hashlib 
import time    
import json 

class Block:  # Define the Block class representing a single block in the blockchain
    def __init__(self, index, data, previous_hash):
        # index: Position of the block in the blockchain
        self.index = index
        # timestamp: Time when the block is created (in seconds since epoch)
        self.timestamp = time.time()
        # data: The actual data or transactions stored in the block
        self.data = data
        # previous_hash: Hash of the previous block in the chain
        self.previous_hash = previous_hash
        # nonce: Number used for mining (proof-of-work)
        self.nonce = 0
        # hash: The hash of the current block, calculated using its contents
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """Calculate the hash of the block"""
        # Serialize the block's contents into a JSON string
        block_string = json.dumps({
            "index": self.index,           # Include block index
            "timestamp": self.timestamp,   # Include timestamp
            "data": self.data,             # Include block data
            "previous_hash": self.previous_hash, # Include previous block's hash
            "nonce": self.nonce            # Include nonce value
        }, sort_keys=True)
        # Calculate SHA-256 hash of the serialized string and return its hexadecimal representation
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty):
        """Simple proof-of-work mining"""
        # target: String of '0's that the hash must start with, based on difficulty
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
