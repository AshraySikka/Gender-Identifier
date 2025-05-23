# Gender-Identifier

This Python program takes user input for gender and identifies it as **Male**, **Female**, **Non-binary / Other**, or indicates if the input is unrecognized. It supports a variety of common gender terms and is case-insensitive.

## 💡 What It Does

- Prompts the user to enter their gender.
- Normalizes the input by trimming spaces and converting to lowercase.
- Checks the input against predefined sets of terms for:
  - Male (`male`, `m`)
  - Female (`female`, `f`)
  - Non-binary / Other (`non-binary`, `nonbinary`, `nb`, `other`, `prefer not to say`, `unknown`)
- Prints the identified gender category or a message if the input doesn't match any known terms.

## 📁 File

- `gender-identifier.py`: Contains the program logic.

## ▶️ How to Run

```bash
python gender-identifier.py
