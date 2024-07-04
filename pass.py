import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

def generate_password():
    length = int(length_entry.get())
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    if not (use_upper or use_lower or use_numbers or use_symbols):
        messagebox.showerror("Error", "Please select at least one character set")
        return

    character_pool = ''
    if use_upper:
        character_pool += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_lower:
        character_pool += 'abcdefghijklmnopqrstuvwxyz'
    if use_numbers:
        character_pool += '0123456789'
    if use_symbols:
        character_pool += '!@#$%^&*()-_=+[]{}|;:,.<>?'

    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4 characters")
        return

    password = []
    if use_upper:
        password.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if use_lower:
        password.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
    if use_numbers:
        password.append(random.choice('0123456789'))
    if use_symbols:
        password.append(random.choice('!@#$%^&*()-_=+[]{}|;:,.<>?'))

    while len(password) < length:
        password.append(random.choice(character_pool))

    random.shuffle(password)
    password = ''.join(password)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Info", "Password copied to clipboard")

app = tk.Tk()
app.title("Advanced Password Generator")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

length_label = tk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(frame, width=5)
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.insert(0, '12')

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

upper_check = tk.Checkbutton(frame, text="Include Uppercase Letters", variable=upper_var)
upper_check.grid(row=1, column=0, columnspan=2, sticky='w')
lower_check = tk.Checkbutton(frame, text="Include Lowercase Letters", variable=lower_var)
lower_check.grid(row=2, column=0, columnspan=2, sticky='w')
numbers_check = tk.Checkbutton(frame, text="Include Numbers", variable=numbers_var)
numbers_check.grid(row=3, column=0, columnspan=2, sticky='w')
symbols_check = tk.Checkbutton(frame, text="Include Symbols", variable=symbols_var)
symbols_check.grid(row=4, column=0, columnspan=2, sticky='w')

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

password_label = tk.Label(frame, text="Generated Password:")
password_label.grid(row=6, column=0, padx=5, pady=5)
password_entry = tk.Entry(frame, width=30)
password_entry.grid(row=6, column=1, padx=5, pady=5)

copy_button = tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=7, column=0, columnspan=2, pady=10)

app.mainloop()
