# 🔐 Random Password Generator

A Python script that generates strong, random passwords based on user input. This tool helps create secure passwords containing a mix of letters, numbers, and symbols.

## 📌 Project Overview
* **Goal:** To automate the creation of secure passwords without human bias.
* **Language:** Python 3.10.12
* **Key Concepts:** Randomization (`random` module), String Manipulation, Input Validation.

## ⚙️ Features
* ✅ **Custom Length:** User can specify how long the password should be.
* ✅ **Strong Security:** Uses uppercase, lowercase, digits, and special symbols.
* ✅ **Error Handling:** Prevents crashing if the user inputs text instead of numbers.

## 🚀 How to Run
1.  Make sure you have Python installed.
2.  Open your terminal or command prompt.
3.  Navigate to the project folder.
4.  Run the script:
    ```bash
    random_pass_generator.py
    ```

## 🧠 How It Works (Logic)
here is the logic breakdown:

1.  **Input:** The script asks for a number (Length). It uses a `while` loop to ensure the input is actually a valid number.
2.  **Ingredients:** It combines `ascii_letters` (A-z), `digits` (0-9), and `punctuation` (!@#) into one big list.
3.  **Selection:** It uses **`random.choices()`** to pick characters.
    * *Why `choices`?* Because it allows duplicates (e.g., a password can have two 'a's), which makes it mathematically harder to crack than `random.sample`.
4.  **Output:** It joins the list of characters into a string and prints it.

## 📚 What I Learned
* How to use the `random` and `string` modules.
* How to handle user errors with `try...except`.
* Difference between `random.choices` (with replacement) and `random.sample` (unique items).
