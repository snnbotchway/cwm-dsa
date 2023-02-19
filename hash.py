import hashlib

# The original message to be hashed
message = "This is a secret message."

# Hash the message using SHA-512
hash_object = hashlib.sha512(message.encode())
original_hash = hash_object.hexdigest()
print("Original Hash:", original_hash)

# Simulate receiving the message
received_message = "This is a secret message"

# Hash the received message using SHA-512
hash_object = hashlib.sha512(received_message.encode())
computed_hash = hash_object.hexdigest()
print("Computed Hash:", computed_hash)

# Compare the computed hash with the received hash
if computed_hash == original_hash:
    print("Message integrity verified.")
else:
    print("Message has been tampered with!")
