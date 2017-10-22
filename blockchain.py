import time
from block import Block
from parameters import Parameters

class BlockChain:

	def __init__(self):
		self.blockchain_list = self.init_chain()

	def tail(self):
		return self.blockchain_list[-1]

	def create_next_block(self, transaction_data):
		timestamp = int(time.time())
		index = len(self.blockchain_list)
		prev_hash = self.tail().hashcode
		para = Parameters(timestamp, index, prev_hash, transaction_data)
		block = Block(para)
		self.blockchain_list.append(block)

	def init_chain(self):
		return [Block.create_genesis()]	

	def print_chain(self):
		for block in self.blockchain_list:
			print("Time: %s" % block.timestamp)
			print("Index: %s" % block.index)
			print("Previous Hashcode: %s" % block.prev_hash)
			print("Data: %s" % block.transaction_data)
			print("Hashcode: %s" % block.hashcode)
<<<<<<< HEAD
			print("================================================================================")
=======
			print("=====================================================")

>>>>>>> cf045df6614baac9a36783792df238fca0c1951b
