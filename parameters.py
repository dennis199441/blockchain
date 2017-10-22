class Parameters:

	def __init__(self, timestamp, index, prev_hash, transaction_data):
		self.timestamp = timestamp
		self.index = index
		self.prev_hash = prev_hash
		self.transaction_data = transaction_data

	@classmethod
	def genesis(cls):
		return cls(0, 0, 0, 'transaction_data')

	def __str__(self):
		return str(self.timestamp) + str(self.index) + str(self.prev_hash) + str(self.transaction_data)