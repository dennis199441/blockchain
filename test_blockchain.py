from blockchain import BlockChain

chain = BlockChain()
chain.create_next_block('data 1')
chain.create_next_block('data 2')
chain.create_next_block('data 3')
chain.create_next_block('data 4')
chain.create_next_block('data 5')
chain.create_next_block('data 6')
chain.create_next_block('data 7')
chain.create_next_block('data 8')
chain.create_next_block('data 9')
chain.create_next_block('data 10')

chain.print_chain()