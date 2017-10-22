# blockchain
This is a simple blockchain implementation.

## Parameters
Parameters objects define the necessary data for Block objects
1. timestamp
2. index
3. previous hashcode
4. transaction data

## Block
Block objects receive Parameters object which stores data.
Once Block object is instantiated, it generates its hashcode.

## BlockChain
BlockChain object links Blocks together. It stores blocks in a list.
Once BlockChain object is instantiated, it creates the genesis block and the block list.
