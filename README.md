# 🔐 Ultimate Password Generator

A Tkinter-based desktop software for generating all possible password patterns that include uppercase/lowercase word variations, numeric values, and special characters — with randomized order for each password.

This tool is currently in active development, and while it performs powerful combinational password generation, it still lacks some advanced password creation features, which are planned for future updates.

---

## 🧩 Features

✅ Dynamic Password Patterns

 Generates unique passwords using a base word combined with numbers and special characters.
 Supports random shuffling for unpredictable patterns.

✅ Customizable Inputs

 Choose how many digits and special characters you want.
 Enter any base word — the program automatically creates case variations.

✅ GUI Interface (Tkinter)

 Easy-to-use graphical interface with options to generate, clear, and save results.
 Scrollable output area for viewing all generated passwords.

✅ Save Functionality

 Save generated passwords to a `.txt` file for later use.

---

## 🛠️ Technologies Used

 Python 3.13.5
 Tkinter (for GUI)
 itertools, random, os (standard Python libraries)

---

## ⚙️ Installation

1. Make sure you have Python 3 installed on your system.

   ```bash
   python --version
   ```

2. Clone or download this repository:

   ```bash
   git clone https://github.com/yourusername/password-pattern-generator.git
   cd password-pattern-generator
   ```

3. Run the program:

   ```bash
   python password_generator.py
   ```

---

## 💡 How It Works

1. Enter your base word (e.g., `Ahad`, `Secure`, `Admin123`).
2. Choose the number of digits and special characters to include.
3. Click Generate — the tool will create hundreds of randomized combinations mixing cases, digits, and symbols.
4. Click Save to export all generated passwords to a text file.

---

## 🚧 Current Limitations

This version is a work in progress.
The program currently:

 Uses limited randomization for speed optimization.
 Does not yet include password strength evaluation or custom rule sets.
 May take longer to generate a very large number of combinations.

> 💬 “I am actively working on it — more advanced password creation options, filtering logic, and stronger entropy checks are planned for future versions.”

---

## 🧠 Planned Future Enhancements

🔹 Password Strength Meter (Entropy Evaluation)
🔹 Option to Include/Exclude Similar Characters (`l`, `1`, `I`, `O`, `0`)
🔹 Copy to Clipboard Function
🔹 Dark/Light Theme Toggle
🔹 Faster Algorithm for Large Word Combinations

---

## 📸 Screenshots (Coming Soon)



---

## 📄 License

This project is open source under the MIT License. You’re free to use, modify, and distribute it with attribution.

---

Author: Abdul Ahad Khan
📅 Project Status: Under Development
💬 Feedback and feature suggestions are always welcome!

---

Would you like me to also generate a short project description (for GitHub repo sidebar) and a requirements.txt file? Both go well with this README.
