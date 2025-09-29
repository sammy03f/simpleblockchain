# Simple Blockchain Implementation

A straightforward blockchain implementation in Python that demonstrates the core concepts without being overly complex.

## What This Blockchain Includes

- **Block Class**: Represents individual blocks with index, timestamp, data, previous hash, and nonce
- **Blockchain Class**: Manages the chain of blocks and provides validation
- **Proof of Work**: Simple mining algorithm that finds hashes starting with a certain number of zeros
- **Chain Validation**: Checks that all blocks are properly linked and have valid hashes
- **Genesis Block**: Automatically creates the first block in the chain

## Files

- `block.py` - The Block class definition
- `blockchain.py` - The Blockchain class that manages the chain
- `demo.py` - A demonstration script showing how to use the blockchain
- `README.md` - This file

## How to Run

1. Make sure you have Python 3.6+ installed
2. Run the demo:
   ```bash
   python demo.py
   ```

## What You'll See

The demo will:
1. Create a new blockchain
2. Add several sample blocks with transaction data
3. Mine each block (this may take a moment due to proof-of-work)
4. Display the entire blockchain
5. Validate the chain integrity

## Key Concepts Demonstrated

- **Hashing**: Each block has a unique hash based on its contents
- **Chain Linking**: Each block references the previous block's hash
- **Proof of Work**: Blocks are "mined" by finding a hash that meets difficulty requirements
- **Immutability**: Changing any block would break the chain validation
- **Validation**: The system can verify the entire chain is intact

## Customization

You can easily modify:
- Mining difficulty (change the `difficulty` parameter)
- Block data (modify the strings in `demo.py`)
- Add more functionality like wallets, transactions, etc.

This is a great starting point for understanding blockchain fundamentals!
