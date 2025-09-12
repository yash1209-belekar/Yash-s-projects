import tkinter as tk
import random

# Character sets
num = list('0123456789')
upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lower = list('abcdefghijklmnopqrstuvwxyz')
specialchar = list('`~!@#$%^&*()_+-=[]{}|/;:,<.>?')

# GUI setup
root = tk.Tk()
root.geometry("600x600+400+200")
root.title("Password Generator")

# Widgets
length_label = tk.Label(root, text='Length:')
length_label.place(x=100, y=20)

length_entry = tk.Text(root, height=1, width=40)
length_entry.place(x=160, y=20)

output_text = tk.Text(root, width=65, height=25)
output_text.place(x=30, y=120)

# Functions
def show_password(password):
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, password)

def generate_simple():
    try:
        n = int(length_entry.get("1.0", 'end-1c').strip())
        password = ''.join(random.choice(upper + lower + num) for _ in range(n))
        show_password(password)
    except ValueError:
        show_password("Please enter a valid number for password length.")

def generate_complex():
    try:
        n = int(length_entry.get("1.0", 'end-1c').strip())
        password = ''.join(random.choice(upper + lower + num + specialchar) for _ in range(n))
        show_password(password)
    except ValueError:
        show_password("Please enter a valid number for password length.")

# Buttons
simple_btn = tk.Button(root, text='Simple', command=generate_simple)
simple_btn.place(x=200, y=80)

complex_btn = tk.Button(root, text='Complex', command=generate_complex)
complex_btn.place(x=350, y=80)

root.mainloop()
