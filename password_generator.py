import random
import string
import tkinter as tk
from tkinter import messagebox

def check_strength(password):
    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if len(password) >= 12:
        score += 1

    if score <= 2:
        return "Weak 🔴"
    elif score == 3 or score == 4:
        return "Medium 🟠"
    else:
        return "Strong 🟢"


def generate_password():
    try:
        length = int(length_entry.get())
    except:
        messagebox.showerror("Error", "Enter valid length")
        return

    chars = string.ascii_lowercase

    if upper_var.get():
        chars += string.ascii_uppercase
    if num_var.get():
        chars += string.digits
    if sym_var.get():
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "Select at least one option")
        return

    password = "".join(random.choice(chars) for _ in range(length))

    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

    strength_label.config(text="Strength: " + check_strength(password))


def copy_password():
    window.clipboard_clear()
    window.clipboard_append(result_entry.get())
    messagebox.showinfo("Copied", "Password copied!")


# UI Window
window = tk.Tk()
window.title("Secure Password Generator")
window.geometry("400x420")
window.config(bg="#1e1e1e")

# Title
tk.Label(window, text="Password Generator", font=("Arial", 16, "bold"),
         bg="#1e1e1e", fg="white").pack(pady=10)

# Length
tk.Label(window, text="Enter Length:", bg="#1e1e1e", fg="white").pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Checkboxes
upper_var = tk.BooleanVar()
num_var = tk.BooleanVar()
sym_var = tk.BooleanVar()

tk.Checkbutton(window, text="Uppercase (A-Z)", variable=upper_var,
               bg="#1e1e1e", fg="white", selectcolor="#333").pack(anchor="w", padx=20)

tk.Checkbutton(window, text="Numbers (0-9)", variable=num_var,
               bg="#1e1e1e", fg="white", selectcolor="#333").pack(anchor="w", padx=20)

tk.Checkbutton(window, text="Symbols (!@#)", variable=sym_var,
               bg="#1e1e1e", fg="white", selectcolor="#333").pack(anchor="w", padx=20)

# Button
tk.Button(window, text="Generate Password", command=generate_password,
          bg="#4CAF50", fg="white").pack(pady=10)

# Result
result_entry = tk.Entry(window, width=30)
result_entry.pack(pady=5)

# Strength label
strength_label = tk.Label(window, text="Strength: -", bg="#1e1e1e", fg="white")
strength_label.pack(pady=5)

# Copy button
tk.Button(window, text="Copy Password", command=copy_password,
          bg="#2196F3", fg="white").pack()

window.mainloop()
