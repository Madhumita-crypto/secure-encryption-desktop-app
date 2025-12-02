import tkinter as tk
from tkinter import messagebox, filedialog
from cryptography.fernet import Fernet
import os

# ---------- KEY MANAGEMENT ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_PATH = os.path.join(BASE_DIR, "secret.key")

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Success", "Secret key generated!")

def load_key():
    return open(KEY_PATH, "rb").read()

# ---------- MESSAGE ENCRYPTION ----------
def encrypt_message():
    try:
        key = load_key()
        fernet = Fernet(key)

        text = input_text.get()
        if not text:
            messagebox.showwarning("Warning", "Enter some text!")
            return

        encrypted = fernet.encrypt(text.encode())
        output_text.delete(0, tk.END)
        output_text.insert(0, encrypted.decode())

    except:
        messagebox.showerror("Error", "Generate key first!")

def decrypt_message():
    try:
        key = load_key()
        fernet = Fernet(key)

        encrypted_text = input_text.get().encode()
        decrypted = fernet.decrypt(encrypted_text).decode()

        output_text.delete(0, tk.END)
        output_text.insert(0, decrypted)

    except:
        messagebox.showerror("Error", "Invalid key or encrypted text!")

# ---------- FILE ENCRYPTION ----------
def encrypt_file():
    try:
        key = load_key()
        fernet = Fernet(key)

        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        with open(file_path, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(file_path + ".enc", "wb") as encrypted_file:
            encrypted_file.write(encrypted)

        messagebox.showinfo("Success", "File encrypted successfully!")

    except:
        messagebox.showerror("Error", "Generate key first!")

def decrypt_file():
    try:
        key = load_key()
        fernet = Fernet(key)

        file_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.enc")])
        if not file_path:
            return

        with open(file_path, "rb") as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        original_path = file_path.replace(".enc", "_decrypted.txt")

        with open(original_path, "wb") as dec_file:
            dec_file.write(decrypted)

        messagebox.showinfo("Success", "File decrypted successfully!")

    except:
        messagebox.showerror("Error", "Invalid encrypted file or key!")

# ---------- GUI WINDOW ----------
root = tk.Tk()
root.title("Secure Encryption System")
root.geometry("520x420")
root.resizable(False, False)

tk.Label(root, text="Secure Encryption System", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(root, text="Input").pack()
input_text = tk.Entry(root, width=65)
input_text.pack(pady=5)

tk.Label(root, text="Output").pack()
output_text = tk.Entry(root, width=65)
output_text.pack(pady=5)

tk.Button(root, text="🔑 Generate Key", width=25, command=generate_key).pack(pady=8)
tk.Button(root, text="🔒 Encrypt Message", width=25, command=encrypt_message).pack(pady=4)
tk.Button(root, text="🔓 Decrypt Message", width=25, command=decrypt_message).pack(pady=4)
tk.Button(root, text="📁 Encrypt File", width=25, command=encrypt_file).pack(pady=4)
tk.Button(root, text="📂 Decrypt File", width=25, command=decrypt_file).pack(pady=4)
tk.Button(root, text="❌ Exit", width=25, command=root.destroy).pack(pady=10)

root.mainloop()
