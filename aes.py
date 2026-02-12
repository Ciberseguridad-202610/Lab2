# Ciberseguridad Laboratorio 2
import os
import sys

from Crypto.Cipher import AES # import AES cipher from the Crypto library
from Crypto.Random import get_random_bytes as rand # import get_random_bytes function to generate random bytes for the key and IV

def encrypt( f: bytes ) -> bytes:
    """
    Encrypts the input file using AES encryption in CBC mode.
    :param f: File to be encrypted, in bytes format.
    :return: Ciphertext of the encrypted file, in bytes format.
    """

    aes = AES.new(rand(16), AES.MODE_CBC) # create a new AES cipher object with a random 16-byte key and CBC mode
    ciphertext = aes.encrypt(f) # encrypt the input file using the AES cipher

    return ciphertext

def decrypt( f: bytes ) -> bytes:
    """
    Decrypts the input file using AES decryption in CBC mode.
    :param f: File to be decrypted, in bytes format.
    :return: Plaintext of the decrypted file, in bytes format.
    """
    aes = AES.new(rand(16), AES.MODE_CBC) # create a new AES cipher object with a random 16-byte key and CBC mode
    plaintext = aes.decrypt(f) # decrypt the input file using the AES cipher

    return plaintext

def run( mode: str, f: bytes ) -> bytes:
    if mode == 'e':
        text = encrypt(f)
        print(">> Encrypted file")

    elif mode == 'd':
        text = decrypt(f)
        print(">> Decrypted file")

    else:
        print(">> Invalid mode. Use 'e' for encryption or 'd' for decryption.")
        return -1

    return text

if __name__ == '__main__':

    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        file_path = sys.argv[2]

        file = os.path.basename(file_path)
        with open(file_path, 'rb') as f:
            text = run(mode, f)

        if text != -1:
            with open(f"{file}.out", 'wb') as f:
                f.write(text)

    else:
        print(">> Please provide the file as a command-line argument.")