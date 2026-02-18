# DEPRECATED
# Key generator V1 for AES encryption. Generates a random 16-byte key and saves it to a file named "k.key".
# Author: Adrian Velasquez

from Crypto.Random import get_random_bytes as rand

@DeprecationWarning
def gen_key():
    """
    Generates a random 16-byte key for AES encryption.
    :return: Randomly generated key, in bytes format.
    """
    k = rand(16) # generate a random 16-byte key
    return k

if __name__ == '__main__':
    key = gen_key()
    with open(f"k.key", 'wb') as f:
        f.write(key)