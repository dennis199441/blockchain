from blockchain import BlockChain

chain = BlockChain()
chain.create_next_block('data 1')
chain.create_next_block('data 2')
chain.create_next_block('data 3')
chain.create_next_block('data 4')
chain.create_next_block('data 5')

chain.print_chain()

print('------------ Modified Data ------------------')

chain.update_data(1, 'modified data 1')
chain.update_data(3, 'modified data 3')
chain.update_data(1, 'modified data 1.1')
chain.update_data(2, 'modified data 2')
chain.update_data(4, 'modified data 4')

chain.print_chain()

i = 0
for i in range(len(chain.blockchain_list)):
	if not chain.blockchain_list[i].is_genesis():
		prev = chain.blockchain_list[i - 1]
		print("Valid Index: %s" % chain.blockchain_list[i].check_valid_index(prev))
		print("Valid prev hash: %s" % chain.blockchain_list[i].check_prev_hash(prev))
		print("Valid hash: %s" % chain.blockchain_list[i].check_valid_hash())