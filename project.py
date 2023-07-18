# 21BCE1975_21BCE1560_21BCE5691_21BCE5353
import tkinter as tk
import string
import random

# Functions to encrypt the message
def caesar_encryption_1(plaintext, key):
    encryption_str = ''
    for i in plaintext:
        if i.isupper():
            temp = 65 + ((ord(i) - 65 + key) % 26)
            encryption_str = encryption_str + chr(temp)
        elif i.islower():
            temp = 97 + ((ord(i) - 97 + key) % 26)
            encryption_str = encryption_str + chr(temp)
        else:
            encryption_str = encryption_str + i
    return encryption_str

def caesar_encryption_2(plaintext, key):
    encryption_str = ''
    for i in plaintext:
        if i.isupper():
            temp = 65 + ((ord(i) - 65 + key) % 26)
            encryption_str = encryption_str + chr(temp)
        elif i.islower():
            temp = 97 + ((ord(i) - 97 + key) % 26)
            encryption_str = encryption_str + chr(temp)
        elif i.isdigit():
            temp = 48 + ((ord(i) - 48 + key) % 10)
            encryption_str = encryption_str + chr(temp)
        else:
            encryption_str = encryption_str + i
    return encryption_str

def caesar_encryption_3(plaintext, key):
    encryption_str = ''
    
    for i in plaintext:
     if True:
            temp = ((ord(i)+key) % 128)
            encryption_str = encryption_str + chr(temp)
    return encryption_str

# Functions to decrypt the message
def caesar_decryption_1(ciphertext, key):
    decryption_str = ''
    for i in ciphertext:
        if i.isupper():
            if ((ord(i) - 65 - key) < 0):
                temp = 65 + ((ord(i) - 65 - key + 26) % 26)
            else:
                temp = 65 + ((ord(i) - 65 - key) % 26)
            decryption_str = decryption_str + chr(temp)
        elif i.islower():
            if ((ord(i) - 97 - key) < 0):
                temp = 97 + ((ord(i) - 97 - key + 26) % 26)
            else:
                temp = 97 + ((ord(i) - 97 - key) % 26)
            decryption_str = decryption_str + chr(temp)
        else:
            decryption_str = decryption_str + i
    return decryption_str

def caesar_decryption_2(ciphertext, key):
    decryption_str = ''
    for i in ciphertext:
        if i.isupper():
            if ((ord(i) - 65 - key) < 0):
                temp = 65 + ((ord(i) - 65 - key + 26) % 26)
            else:
                temp = 65 + ((ord(i) - 65 - key) % 26)
            decryption_str = decryption_str + chr(temp)
        elif i.islower():
            if ((ord(i) - 97 - key) < 0):
                temp = 97 + ((ord(i) - 97 - key + 26) % 26)
            else:
                temp = 97 + ((ord(i) - 97 - key) % 26)
            decryption_str = decryption_str + chr(temp)
        elif i.isdigit():
            if ((ord(i) - 48 - key) < 0):
                temp = 48 + ((ord(i) - 48 - key + 10) % 10)
            else:
                temp = 48 + ((ord(i) - 48 - key) % 10)
            decryption_str = decryption_str + chr(temp)
        else:
            decryption_str = decryption_str + i
    return decryption_str

def caesar_decryption_3(ciphertext, key):
    decryption_str = ''
    for i in ciphertext:
        if True:
            if ((ord(i)- key) < 0):
                temp = ((ord(i) - key + 128) % 128)
            else:
                temp = ((ord(i) - key) % 128)
            decryption_str = decryption_str + chr(temp)

    return decryption_str

# Functions to handle the encryption button click event
def encrypt_message():
    message = message_entry.get()
    key = int(key_entry.get())
    option = option_var.get()
    if option == "Only Alphabets":
        message = encrypted_message = caesar_encryption_1(message, key)
    elif option == "Alphabets and Numbers":
        message = encrypted_message = caesar_encryption_2(message, key)
    elif option == "Alphabets, Numbers and Symbols":
        message = encrypted_message = caesar_encryption_3(message, key)
    else:
        pass
    encrypted_text.delete('1.0', tk.END)
    encrypted_text.insert(tk.END, encrypted_message)

# Function to handle the decryption button click event
def decrypt_message():
    message = message_entry.get()
    key = int(key_entry.get())
    option = option_var.get()
    if option == "Only Alphabets":
        message = decrypted_message = caesar_decryption_1(message, key)
    elif option == "Alphabets and Numbers":
        message = decrypted_message = caesar_decryption_2(message, key)
    else:
        message = decrypted_message = caesar_decryption_3(message, key)
    
    decrypted_text.delete('1.0', tk.END)
    decrypted_text.insert(tk.END, decrypted_message)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher Encryption and Decryption (ISAA Project)")
root.configure(bg="#2c3e50")

# Create the input frame
input_frame = tk.Frame(root, bg="#2c3e50")
input_frame.pack(padx=20, pady=20)

# Create the message label and entry box
message_label = tk.Label(input_frame, text="Message:", font=("Helvetica", 14), fg="#ecf0f1", bg="#2c3e50")
message_label.grid(row=0, column=0, padx=10, pady=10)
message_entry = tk.Entry(input_frame, font=("Helvetica", 14), bg="#ecf0f1", fg="#000000",width=40)
message_entry.grid(row=0, column=1, padx=10, pady=10)

# Create the key label and entry box
key_label = tk.Label(input_frame, text="Key:         ", font=("Helvetica", 14), fg="#ecf0f1", bg="#2c3e50")
key_label.grid(row=1, column=0, padx=10, pady=10)
key_entry = tk.Entry(input_frame, font=("Helvetica", 14), bg="#ecf0f1", fg="#000000",width=40)
key_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the options label and dropdown menu
option_label = tk.Label(input_frame, text="Options:  ", font=("Helvetica", 14), fg="#ecf0f1", bg="#2c3e50")
option_label.grid(row=2, column=0, padx=10, pady=10)
option_var = tk.StringVar(input_frame)
option_var.set("Only Alphabets")
option_menu = tk.OptionMenu(input_frame, option_var, "Only Alphabets", "Alphabets and Numbers", "Alphabets, Numbers and Symbols")
option_menu.config(font=("Helvetica", 14), bg="#ecf0f1", fg="#000000")
option_menu.grid(row=2, column=1, padx=10, pady=10)

# Create the encryption and decryption buttons
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(padx=20, pady=(0,20))
encrypt_button = tk.Button(button_frame, text="Encrypt", font=("Helvetica", 14), bg="#00ba54", fg="#ffffff", command=encrypt_message)
encrypt_button.pack(side=tk.LEFT, padx=10)
decrypt_button = tk.Button(button_frame, text="Decrypt", font=("Helvetica", 14), bg="#de043e", fg="#ffffff", command=decrypt_message)
decrypt_button.pack(side=tk.LEFT, padx=10)

# Create the output frame
output_frame = tk.Frame(root, bg="#2c3e50")
output_frame.pack(padx=20, pady=(0,20))

# Create the encrypted message label and text box
encrypted_label = tk.Label(output_frame, text="Encrypted Message:", font=("Helvetica", 14), fg="#ffffff", bg="#00ba54")
encrypted_label.grid(row=0, column=0, padx=10, pady=10)
encrypted_text = tk.Text(output_frame, height=5, font=("Helvetica", 14), bg="#000000", fg="#00ba54")
encrypted_text.grid(row=1, column=0, padx=10)

# Create the decrypted message label and text box
decrypted_label = tk.Label(output_frame, text="Decrypted Message:", font=("Helvetica", 14), fg="#ffffff", bg="#de043e")
decrypted_label.grid(row=2, column=0, padx=10, pady=(20,10))
decrypted_text = tk.Text(output_frame, height=5, font=("Helvetica", 14), bg="#000000", fg="#de043e")
decrypted_text.grid(row=3, column=0, padx=10)

root.mainloop()


"""
import tkinter as tk

# Function to encrypt the message
def caesar_encryption(plaintext, key):
    encryption_str = ''
    for i in plaintext:
        if i.isupper():
            temp = 65 + ((ord(i) - 65 + key) % 26)
            encryption_str = encryption_str + chr(temp)
        elif i.islower():
            temp = 97 + ((ord(i) - 97 + key) % 26)
            encryption_str = encryption_str + chr(temp)
        else:
            encryption_str = encryption_str + i
    return encryption_str

# Function to decrypt the message
def caesar_decryption(ciphertext, key):
    decryption_str = ''
    for i in ciphertext:
        if i.isupper():
            if ((ord(i) - 65 - key) < 0):
                temp = 65 + ((ord(i) - 65 - key + 26) % 26)
            else:
                temp = 65 + ((ord(i) - 65 - key) % 26)
            decryption_str = decryption_str + chr(temp)
        elif i.islower():
            if ((ord(i) - 97 - key) < 0):
                temp = 97 + ((ord(i) - 97 - key + 26) % 26)
            else:
                temp = 97 + ((ord(i) - 97 - key) % 26)
            decryption_str = decryption_str + chr(temp)
        else:
            decryption_str = decryption_str + i
    return decryption_str

# Function to handle the encryption button click event
def encrypt_message():
    message = message_entry.get()
    key = int(key_entry.get())
    encrypted_message = caesar_encryption(message, key)
    encrypted_text.delete('1.0', tk.END)
    encrypted_text.insert(tk.END, encrypted_message)

# Function to handle the decryption button click event
def decrypt_message():
    message = message_entry.get()
    key = int(key_entry.get())
    decrypted_message = caesar_decryption(message, key)
    decrypted_text.delete('1.0', tk.END)
    decrypted_text.insert(tk.END, decrypted_message)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher Encryption and Decryption")
root.configure(bg="#2c3e50")

# Create the labels
message_label = tk.Label(root, text="Message:", fg="#ecf0f1", bg="#2c3e50")
message_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

key_label = tk.Label(root, text="Key:", fg="#ecf0f1", bg="#2c3e50")
key_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

encrypted_label = tk.Label(root, text="Encrypted Message:", fg="#ecf0f1", bg="#2c3e50")
encrypted_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

decrypted_label = tk.Label(root, text="Decrypted Message:", fg="#ecf0f1", bg="#2c3e50")
decrypted_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Create the entry fields
message_entry = tk.Entry(root, width=50)
message_entry.grid(row=0, column=1, padx=10, pady=10)

key_entry = tk.Entry(root, width=50)
key_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the text boxes
encrypted_text = tk.Text(root, height=5, width=50, bg="#000608", fg="#00ff2a")
encrypted_text.grid(row=2, column=1, padx=10, pady=10)

decrypted_text = tk.Text(root, height=5, width=50, bg="#000608", fg="#ff0d15")
decrypted_text.grid(row=3, column=1, padx=10, pady=10)

# Create the buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message, bg="#27ae60", fg="#ecf0f1")
encrypt_button.grid(row=4, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message, bg="#c0392b", fg="#ecf0f1")
decrypt_button.grid(row=4, column=1, padx=10, pady=10)

# Run the main loop
root.mainloop()
############################################################################
import tkinter as tk

# Function to encrypt the message
def caesar_encryption(plaintext, key):
    encryption_str = ''
    for i in plaintext:
        if i.isupper():
            temp = 65 + ((ord(i) - 65 + key) % 26)
            encryption_str = encryption_str + chr(temp)
        elif i.islower():
            temp = 97 + ((ord(i) - 97 + key) % 26)
            encryption_str = encryption_str + chr(temp)
        else:
            encryption_str = encryption_str + i
    return encryption_str

# Function to decrypt the message
def caesar_decryption(ciphertext, key):
    decryption_str = ''
    for i in ciphertext:
        if i.isupper():
            if ((ord(i) - 65 - key) < 0):
                temp = 65 + ((ord(i) - 65 - key + 26) % 26)
            else:
                temp = 65 + ((ord(i) - 65 - key) % 26)
            decryption_str = decryption_str + chr(temp)
        elif i.islower():
            if ((ord(i) - 97 - key) < 0):
                temp = 97 + ((ord(i) - 97 - key + 26) % 26)
            else:
                temp = 97 + ((ord(i) - 97 - key) % 26)
            decryption_str = decryption_str + chr(temp)
        else:
            decryption_str = decryption_str + i
    return decryption_str

# Function to handle the encryption button click event
def encrypt_message():
    message = message_entry.get()
    key = int(key_entry.get())
    encrypted_message = caesar_encryption(message, key)
    encrypted_text.delete('1.0', tk.END)
    encrypted_text.insert(tk.END, encrypted_message)

# Function to handle the decryption button click event
def decrypt_message():
    message = message_entry.get()
    key = int(key_entry.get())
    decrypted_message = caesar_decryption(message, key)
    decrypted_text.delete('1.0', tk.END)
    decrypted_text.insert(tk.END, decrypted_message)

# Create the main window
root = tk.Tk()

# Set the window title and size
root.title("Caesar Cipher Encryption and Decryption")
root.geometry("600x400")

# Create the message label and entry box
message_label = tk.Label(root, text="Enter your message:")
message_label.pack(pady=10)

message_entry = tk.Entry(root, width=50)
message_entry.pack()

# Create the key label and entry box
key_label = tk.Label(root, text="Enter the shift value/key:")
key_label.pack(pady=10)

key_entry = tk.Entry(root, width=50)
key_entry.pack()

# Create the encryption button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.pack(pady=20)

# Create the encrypted message label and text box
encrypted_label = tk.Label(root, text="Encrypted message:")
encrypted_label.pack()

encrypted_text = tk.Text(root, height=5, width=50)
encrypted_text.pack()

# Create the decryption button
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message)
decrypt_button.pack(pady=20)

# Create the decrypted message label and text box
decrypted_label = tk.Label(root, text="Decrypted message:")
decrypted_label.pack()

decrypted_text = tk.Text(root, height=5, width=50)
decrypted_text.pack()

# Run the main loop
root.mainloop()

########################################################################################
message = '21BCE197521BCE156021BCE569121BCE5353'
encrypted = ''
decrypted = ''
key = 5
def caesar_encryption(plaintext, key):
 encryption_str = ''
 for i in plaintext:
    if i.isupper():
        temp = 65 + ((ord(i) - 65 + key) % 26)
        encryption_str = encryption_str + chr(temp)
    elif i.islower():
        temp = 97 + ((ord(i) - 97 + key) % 26)
        encryption_str = encryption_str + chr(temp)
    else:
        encryption_str = encryption_str + i

 return encryption_str

def caesar_decryption(ciphertext, key):
 decryption_str = ''
 for i in ciphertext:
    if i.isupper():
        if ((ord(i) - 65 - key) < 0):
            temp = 65 + ((ord(i) - 65 - key + 26) % 26)
        else:
            temp = 65 + ((ord(i) - 65 - key) % 26)
            decryption_str = decryption_str + chr(temp)
    elif i.islower():
        if ((ord(i) - 97 - key) < 0):
            temp = 97 + ((ord(i) - 97 - key + 26) % 26)
        else:
            temp = 97 + ((ord(i) - 97 - key) % 26)
            decryption_str = decryption_str + chr(temp)
    else:
        decryption_str = decryption_str + i
 return decryption_str

encrypted = caesar_encryption(message, key)
decrypted = caesar_decryption(encrypted, key)
print("The message text is :", message)
print("The shift value/key is :", key)
print("The encrypted text is :", encrypted)
print("The decrypted text is :", decrypted)
"""