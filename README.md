# Caesar Cipher Encryptor & Decryptor

A simple Python script that allows you to *encrypt* or *decrypt* messages using the Caesar Cipher technique. The Caesar Cipher is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## 🔐 Features

* Encrypts text using a custom shift value
* Decrypts text using the same shift value
* Handles both uppercase and lowercase letters
* Leaves non-alphabet characters unchanged

## 📜 How It Works

1. The user is prompted to choose between encryption and decryption.
2. The user inputs the message.
3. The user enters a shift value (positive integer).
4. The program performs Caesar Cipher encryption/decryption and displays the result.

## 🧑‍💻 Usage

### Requirements

* Python 3.x

### Run the script

bash
python caesar_cipher.py


### Example


Caesar Cipher Encryption & Decryption
Type 'e' to encrypt or 'd' to decrypt: e
Enter the message: Hello, World!
Enter the shift value (e.g., 3): 3
Encrypted message: Khoor, Zruog!


## 🗂 File Structure


caesar_cipher.py   # Main Python script
README.md          # Project description


## 📌 Notes

* Use the same shift value to decrypt the message that was used to encrypt it.
* Non-alphabet characters (e.g., punctuation, spaces) are not modified.

## 📄 License

This project is licensed under the MIT License.

---

