import hashlib

# Function to hash passwords
def hash_pwd(value):
    return hashlib.sha256(value.encode()).hexdigest()