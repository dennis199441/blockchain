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

	def update_data(self, index, transaction_data):
		timestamp = int(time.time())

		if index != 0:
			prev_hash = self.blockchain_list[index - 1].hashcode
		else:
			prev_hash = 0

		para = Parameters(timestamp, index, prev_hash, transaction_data)
		self.blockchain_list[index].update_para(para)
	
		i = index + 1
		for i in range(len(self.blockchain_list)):
			self.blockchain_list[i].prev_hash = self.blockchain_list[i - 1].hashcode
			self.blockchain_list[i].recalculate_hash()

	def print_chain(self):
		for block in self.blockchain_list:
			print("Time: %s" % block.timestamp)
			print("Index: %s" % block.index)
			print("Previous Hashcode: %s" % block.prev_hash)
			print("Data: %s" % block.transaction_data)
			print("Hashcode: %s" % block.hashcode)
			print("\n")

