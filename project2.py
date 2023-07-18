import tkinter as tk

# Define the encryption function
def encrypt_message():
    original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890!@#$%\\&*()-_=+{[]|}/?.,><:;"
    key      = "q&ertyP}A?SDF(GHJ;KLjk:1{zxTYUI,m|QWE-R=95>160ZX<C/u_io@+$sdfg[h.VBNM7\\!#2cvb]n)03pa*84% w"
    message = message_entry.get()
    encrypted = ''
    for i in message:
        if i in original:
            encrypted = encrypted + key[original.find(i)]
        else:
            encrypted = encrypted + i
    encrypted_text.config(state='normal')
    encrypted_text.delete(1.0, tk.END)
    encrypted_text.insert(tk.END, encrypted)
    encrypted_text.config(state='disabled')

# Define the decryption function
def decrypt_message():
    original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890!@#$%\\&*()-_=+{[]|}/?.,><:;"
    key      = "q&ertyP}A?SDF(GHJ;KLjk:1{zxTYUI,m|QWE-R=95>160ZX<C/u_io@+$sdfg[h.VBNM7\\!#2cvb]n)03pa*84% w"
    message = message_entry.get()
    decrypted = ''
    for i in message:
        if i in key:
            decrypted = decrypted + original[key.find(i)]
        else:
            decrypted = decrypted + i
    decrypted_text.config(state='normal')
    decrypted_text.delete(1.0, tk.END)
    decrypted_text.insert(tk.END, decrypted)
    decrypted_text.config(state='disabled')

# Create the tkinter window
window = tk.Tk()
window.title("Message Encryption and Decryption")
window.configure(bg='#121212')

# Create the message entry box
message_label = tk.Label(window, text="Enter your message:", bg='#121212', fg='#ffffff')
message_label.pack()
message_entry = tk.Entry(window, bg='#212121', fg='#ffffff', bd=0, highlightthickness=1, highlightcolor='#444444', highlightbackground='#444444',width=50)
message_entry.pack(padx=10, pady=10)

# Create the encrypt button
encrypt_button = tk.Button(window, text="Encrypt Message", command=encrypt_message, bg='#ffffff', fg='#121212', bd=0, activebackground='#eeeeee', activeforeground='#121212')
encrypt_button.pack(pady=10)

# Create the decrypt button
decrypt_button = tk.Button(window, text="Decrypt Message", command=decrypt_message, bg='#ffffff', fg='#121212', bd=0, activebackground='#eeeeee', activeforeground='#121212')
decrypt_button.pack(pady=10)

# Create the encrypted text box
encrypted_label = tk.Label(window, text="Encrypted Message:", bg='#121212', fg='#ffffff')
encrypted_label.pack()
encrypted_text = tk.Text(window, height=5, bg='#212121', fg='#ffffff', bd=0, highlightthickness=1, highlightcolor='#444444', highlightbackground='#444444')
encrypted_text.pack(padx=10, pady=10)

# Create the decrypted text box
decrypted_label = tk.Label(window, text="Decrypted Message:", bg='#121212', fg='#ffffff')
decrypted_label.pack()
decrypted_text = tk.Text(window, height=5, bg='#212121', fg='#ffffff', bd=0, highlightthickness=1, highlightcolor='#444444', highlightbackground='#444444')
decrypted_text.pack(padx=10, pady=10)

# Run the tkinter event loop
window.mainloop()


"""message   = '21BCE1975_21BCE1560_21BCE5691_21BCE5353'
encrypted = ''

original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890!@#$%\&*()-_=+{}[]|/?.,><:;"

key      = "q&ertyP}A?SDF(GHJ;KLjk:1{zxTYUI,m|QWE-R=95>160ZX<C/u_io@+$sdfg[h.VBNM7\!#2cvb]n)03pa*84% w"

for i in message:
 if i in original:
  encrypted = encrypted + key[original. find(i)]
 else:
  encrypted = encrypted + i

print("The message text is :" , message)
print("The original characters order is :" , original)
print("The substituted characters order is :" , key)
print("The encrypted text is :", encrypted)

"""



