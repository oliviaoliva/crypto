import time
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# Criptografia simétrica com AES
def encrypt_symmetric(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    
    return cipher.nonce, tag, ciphertext

# Criptografia assimétrica com RSA
def encrypt_asymmetric(file_path, public_key_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    recipient_key = RSA.import_key(open(public_key_path).read())
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    ciphertext = cipher_rsa.encrypt(data)
    
    return ciphertext

# Gerar chave para criptografia simétrica
symmetric_key = get_random_bytes(16)

# Gerar par de chaves para criptografia assimétrica
key = RSA.generate(2048)
private_key_path = 'private_key.pem'
public_key_path = 'public_key.pem'
with open(private_key_path, 'wb') as file:
    file.write(key.export_key())
with open(public_key_path, 'wb') as file:
    file.write(key.publickey().export_key())

# Criptografar o arquivo usando os dois métodos
start_time = time.time()
symmetric_result = encrypt_symmetric('arquivo.txt', symmetric_key)
symmetric_time = time.time() - start_time

start_time = time.time()
asymmetric_result = encrypt_asymmetric('arquivo.txt', public_key_path)
asymmetric_time = time.time() - start_time

# Comparar os tempos de processamento
print('Tempo de criptografia simétrica: {:.4f} segundos'.format(symmetric_time))
print('Tempo de criptografia assimétrica: {:.4f} segundos'.format(asymmetric_time))
