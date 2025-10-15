import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import random
import itertools

# Special characters set
SPECIAL_CHARS = "~!@#$%^&*()_+`\\}\"[{];:|.,>?<-="


def generate_all_passwords(base_word, num_digits, num_specials):
    """
    Generates all possible unique passwords based on:
    - upper/lower combinations of the word
    - number combinations (up to user-defined digits)
    - special character combinations (up to user-defined specials)
    - random shuffling of components
    """
    results = set()

    # All upper/lowercase combinations for the word
    cases = set(map(''.join, itertools.product(*((c.lower(), c.upper()) for c in base_word))))

    numbers = [str(i) for i in range(10)]

    # Generate all possible combinations for specials (with limited randomization)
    special_combos = []
    for _ in range(50):  # limit for speed
        combo = ''.join(random.choices(SPECIAL_CHARS, k=num_specials))
        special_combos.append(combo)

    for word_case in cases:
        for _ in range(100):  # create variations for numbers to keep it fast
            num_combo = ''.join(random.choices(numbers, k=num_digits))
            for special in special_combos:
                base = word_case + num_combo + special
                mixed = list(base)
                random.shuffle(mixed)
                results.add(''.join(mixed))

    return list(results)


# ----------- Tkinter GUI -------------
def create_gui():
    def generate():
        word = entry_word.get().strip()
        try:
            num_digits = int(entry_digits.get())
            num_specials = int(entry_specials.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numbers for digits and specials.")
            return

        if not word:
            messagebox.showwarning("Warning", "Please enter a base word.")
            return
        if num_digits < 1 or num_specials < 1:
            messagebox.showwarning("Warning", "Values must be greater than zero.")
            return

        passwords = generate_all_passwords(word, num_digits, num_specials)
        output_box.delete(1.0, tk.END)
        for pwd in passwords:
            output_box.insert(tk.END, pwd + "\n")

        messagebox.showinfo("Done", f"Generated {len(passwords)} unique passwords!")

    def save_to_file():
        data = output_box.get(1.0, tk.END).strip()
        if not data:
            messagebox.showwarning("Warning", "No passwords to save!")
            return
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file:
            with open(file, "w") as f:
                f.write(data)
            messagebox.showinfo("Saved", f"Passwords saved to {file}")

    def clear_output():
        output_box.delete(1.0, tk.END)
        entry_word.delete(0, tk.END)
        entry_digits.delete(0, tk.END)
        entry_specials.delete(0, tk.END)

    # Main window
    root = tk.Tk()
    root.title("🔐 Ultimate Password Pattern Generator")
    root.geometry("650x600")
    root.config(bg="#2D1115")

    # Title label
    tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="#2D1115", fg="white").pack(pady=10)

    # Input frame
    frame = tk.Frame(root, bg="#2D1115")
    frame.pack(pady=10)

    tk.Label(frame, text="Base Word:", font=("Arial", 12), bg="#2D1115", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_word = tk.Entry(frame, width=20, font=("Arial", 12))
    entry_word.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Number of Digits:", font=("Arial", 12), bg="#2D1115", fg="white").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_digits = tk.Entry(frame, width=20, font=("Arial", 12))
    entry_digits.insert(0, "2")
    entry_digits.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame, text="Special Characters:", font=("Arial", 12), bg="#2D1115", fg="white").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_specials = tk.Entry(frame, width=20, font=("Arial", 12))
    entry_specials.insert(0, "2")
    entry_specials.grid(row=2, column=1, padx=5, pady=5)

    # Button frame
    btn_frame = tk.Frame(root, bg="#2D1115")
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Generate", font=("Arial", 12), bg="#4CAF50", fg="white", command=generate).grid(row=0, column=0, padx=8)
    tk.Button(btn_frame, text="Save", font=("Arial", 12), bg="#2196F3", fg="white", command=save_to_file).grid(row=0, column=1, padx=8)
    tk.Button(btn_frame, text="Clear", font=("Arial", 12), bg="#F44336", fg="white", command=clear_output).grid(row=0, column=2, padx=8)

    # Output area
    output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=75, height=20, font=("Courier", 10))
    output_box.pack(padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
