from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Set up the encryption key (must be 16, 24, or 32 bytes long)
key = b'secret_key_12345'


def encrypt_user_id(user_id):
    # Convert user ID to bytes
    user_id_bytes = str(user_id).encode('utf-8')

    # Set up the cipher and encrypt the user ID
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(user_id_bytes, AES.block_size))

    # Encode the cipher_text as base64 and return it along with the initialization vector
    return base64.b64encode(cipher.iv + cipher_text)


def decrypt_user_id(encrypted_user_id):
    # Decode the base64-encoded cipher_text and initialization vector
    encrypted_user_id = base64.b64decode(encrypted_user_id)
    iv = encrypted_user_id[:AES.block_size]
    cipher_text = encrypted_user_id[AES.block_size:]

    # Set up the cipher and decrypt the cipher_text
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(cipher_text), AES.block_size)

    # Convert the decrypted user ID to a string and return it
    return plaintext.decode('utf-8')


cipher = encrypt_user_id(7654)
print(cipher)
print(decrypt_user_id(cipher))
