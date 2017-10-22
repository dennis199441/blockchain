import hashlib
from parameters import Parameters

class Block:

	def __init__(self, para):
		self.timestamp = para.timestamp
		self.index = para.index
		self.prev_hash = para.prev_hash
		self.transaction_data = para.transaction_data
		self.hashcode = self.generate_hashcode()

	def para(self):
		return Parameters(self.timestamp, self.index, self.prev_hash, self.transaction_data)

	@classmethod
	def create_genesis(cls):
		para = Parameters.genesis()
		return Block(para)

	def generate_hashcode(self):
		return hashlib.sha256(str(self.para()).encode()).hexdigest()

