import hashlib
import time

def proof_of_work(block_data, difficulty=4):
    nonce = 0
    prefix = '0' * difficulty
    while True:
        text = f"{block_data}{nonce}"
        hash_result = hashlib.sha256(text.encode()).hexdigest()
        if hash_result.startswith(prefix):
            return nonce, hash_result
        nonce += 1

start = time.time()
block_data = "block #1 transaction data"
nonce, hash_found = proof_of_work(block_data)
end = time.time()

print(f"✅ Block mined with nonce: {nonce}")
print(f"⛓ Hash: {hash_found}")
print(f"⏱ Time taken: {end - start:.2f} seconds")
