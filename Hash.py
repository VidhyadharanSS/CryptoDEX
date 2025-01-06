315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3 : Hash key

import hashlib

# Create a hash object using SHA-256
hash_object = hashlib.sha256()

# Update the hash object with the data to be hashed
data = b'Hello, world!'
hash_object.update(data)

# Get the hashed data as a hexadecimal string
hashed_data = hash_object.hexdigest()

print(hashed_data)
