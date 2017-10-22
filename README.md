# blockchain
This is a simple blockchain implementation. 
There are three objects:
1. Parameters
2. Block
3. BlockChain

## Parameters
Parameters objects define the necessary data for Block objects
1. timestamp
2. index
3. previous hashcode
4. transaction data

## Block
Block receives Parameters object which stores data.
Once Block object is instantiated, it generates its hashcode.

## BlockChain
BlockChain links Blocks together. It stores blocks in a list.
Once BlockChain object is instantiated, it creates the genesis block and the block list.
