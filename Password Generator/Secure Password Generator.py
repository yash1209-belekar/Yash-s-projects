import tkinter as tk
from tkinter import messagebox
import secrets
import string

# Character sets
num = string.digits
upper = string.ascii_uppercase
lower = string.ascii_lowercase
specialchar = string.punctuation

# GUI setup
root = tk.Tk()
root.geometry("600x650+400+200")
root.title("Secure Password Generator")

# Widgets
length_label = tk.Label(root, text='Length:', font=('Arial', 10))
length_label.place(x=100, y=20)

length_entry = tk.Entry(root, width=40, font=('Arial', 10))
length_entry.place(x=160, y=20)

output_label = tk.Label(root, text='Generated Password:', font=('Arial', 10))
output_label.place(x=30, y=70)

output_text = tk.Text(root, width=65, height=20)
output_text.place(x=30, y=100)

# Functions
def show_password(password):
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, password)

def copy_to_clipboard():
    """Copy generated password to clipboard"""
    password = output_text.get('1.0', tk.END).strip()
    if password and "Please enter" not in password and "Password length" not in password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy. Generate one first!")

def generate_simple():
    """Generate simple password (letters and numbers only)"""
    try:
        n = int(length_entry.get().strip())
        
        # Validation
        if n <= 0:
            show_password("Error: Password length must be at least 1")
            return
        if n > 500:
            show_password("Error: Password length cannot exceed 500 characters")
            return
        
        # Ensure at least one character from each category
        password = [
            secrets.choice(upper),
            secrets.choice(lower),
            secrets.choice(num)
        ]
        
        # Fill remaining length with random characters
        all_chars = upper + lower + num
        password += [secrets.choice(all_chars) for _ in range(n - 3)]
        
        # Shuffle to randomize positions
        secrets.SystemRandom().shuffle(password)
        show_password(''.join(password))
        
    except ValueError:
        show_password("Error: Please enter a valid number for password length.")

def generate_complex():
    """Generate complex password (includes special characters)"""
    try:
        n = int(length_entry.get().strip())
        
        # Validation
        if n <= 0:
            show_password("Error: Password length must be at least 1")
            return
        if n > 500:
            show_password("Error: Password length cannot exceed 500 characters")
            return
        
        # Ensure at least one character from each category
        password = [
            secrets.choice(upper),
            secrets.choice(lower),
            secrets.choice(num),
            secrets.choice(specialchar)
        ]
        
        # Fill remaining length with random characters
        all_chars = upper + lower + num + specialchar
        password += [secrets.choice(all_chars) for _ in range(n - 4)]
        
        # Shuffle to randomize positions
        secrets.SystemRandom().shuffle(password)
        show_password(''.join(password))
        
    except ValueError:
        show_password("Error: Please enter a valid number for password length.")

# Buttons
simple_btn = tk.Button(root, text='Simple', command=generate_simple, font=('Arial', 10), width=12)
simple_btn.place(x=150, y=50)

complex_btn = tk.Button(root, text='Complex', command=generate_complex, font=('Arial', 10), width=12)
complex_btn.place(x=300, y=50)

copy_btn = tk.Button(root, text='Copy to Clipboard', command=copy_to_clipboard, font=('Arial', 10), width=20)
copy_btn.place(x=180, y=590)

root.mainloop()
