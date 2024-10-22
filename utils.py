from cryptography.fernet import Fernet

# Gerar uma chave e salvar em um arquivo (fazer isso uma única vez)
def generate_key():
    key = Fernet.generate_key()
    with open("data/secret.key", "wb") as key_file:
        key_file.write(key)

# Carregar a chave
def load_key():
    return open("data/secret.key", "rb").read()

# Criptografar o conteúdo do arquivo JSON
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Descriptografar o conteúdo do arquivo JSON
def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)

# Desencripitar json
#key = load_key()
#decrypt_file("data/passwords.json", key)

#Encripitar json
# key = load_key()
# encrypt_file("data/passwords.json", key)

