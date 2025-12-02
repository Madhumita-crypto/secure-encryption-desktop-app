from cryptography.fernet import Fernet

# Generate a key (run only once and save the key)
import os
from cryptography.fernet import Fernet

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_PATH = os.path.join(BASE_DIR, "secret.key")

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as key_file:
        key_file.write(key)

def load_key():
    return open(KEY_PATH, "rb").read()


# Encrypt a message
def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Encrypt a file
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print("✅ File encrypted successfully!")

# Decrypt a file
def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    original_path = file_path.replace(".enc", "")

    with open(original_path, "wb") as dec_file:
        dec_file.write(decrypted)

    print("✅ File decrypted successfully!")

while True:
    print("\n🔐 Secure Encryption System")
    print("1. Generate Key")
    print("2. Encrypt Message")
    print("3. Decrypt Message")
    print("4. Encrypt File")
    print("5. Decrypt File")
    print("0. Exit")

    choice = input("Enter your choice (0/1/2/3/4/5): ")

    if choice == "1":
        generate_key()
        print("✅ Secret key generated and saved as secret.key")

    elif choice == "2":
        text = input("Enter message to encrypt: ")
        encrypted = encrypt_message(text)
        print("🔒 Encrypted Message:", encrypted)

    elif choice == "3":
        encrypted_text = input("Enter encrypted message: ").encode()
        decrypted = decrypt_message(encrypted_text)
        print("🔓 Decrypted Message:", decrypted)

    elif choice == "4":
        path = input("Enter full file path to encrypt: ").strip().strip('"')
        encrypt_file(path)

    elif choice == "5":
        path = input("Enter full encrypted file path (.enc): ").strip().strip('"')
        decrypt_file(path)

    elif choice == "0":
        print("👋 Exiting Secure Encryption System. Stay safe!")
        break

    else:
        print("❌ Invalid choice. Try again.")

    # ----- CONTINUE OR EXIT PROMPT -----
    again = input("\nDo you want to continue? (y/n): ").lower()

    if again != "y":
        print("👋 Exiting Secure Encryption System. Stay safe!")
        break


'''print("🔐 Secure Encryption System")
print("1. Generate Key")
print("2. Encrypt Message")
print("3. Decrypt Message")
print("4. Encrypt File")
print("5. Decrypt File")

choice = input("Enter your choice (1/2/3/4/5): ")


if choice == "1":
    generate_key()
    print("✅ Secret key generated and saved as secret.key")

elif choice == "2":
    text = input("Enter message to encrypt: ")
    encrypted = encrypt_message(text)
    print("🔒 Encrypted Message:", encrypted)

elif choice == "3":
    encrypted_text = input("Enter encrypted message: ").encode()
    decrypted = decrypt_message(encrypted_text)
    print("🔓 Decrypted Message:", decrypted)

elif choice == "4":
    path=input("Enter full file path to encrypt:")
    encrypt_file(path)

elif choice=="5":
    path=input("Enter full encrypted file path (.enc):")
    decrypt_file(path)
else:
    print("❌ Invalid choice")'''
