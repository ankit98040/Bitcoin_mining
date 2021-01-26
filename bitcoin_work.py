from hashlib import sha256
MAX_NONCE=1000000000

def SHA256(text):
	return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
	prefix_str = '0'*prefix_zeros
	for nonce in range(MAX_NONCE):
		text = str(block_number) + transactions + previous_hash + str(nonce)
		new_hash = SHA256(text)

		if new_hash.startswith(prefix_str):
			print(f"Yay! Successfully mined bitcoin with nonce value:{nonce}")
			print()
			return new_hash

	raise BaseException(f"Could not find value of nonce after trying {MAX_NONCE} times")
	

if __name__=='__main__':
	transactions='''
	Ankit->Rakesh->25,
	raj->rohit->65,
	tiger->hrithik->-1000
	'''

	difficulty=6 #number of zeros
	import time
	start = time.time()
	print("Mining start")
	print()
	new_hash = mine(5,transactions,'a815eaee566f993e1413aaee8874587c66729d006180c5ce29c67e8f79daabb2', difficulty)
	total_time = str((time.time() - start))

	print(f"Mining ended. Total Mining process took: {total_time} seconds")
	print()
	print(f"the hash value is: {new_hash} ")


