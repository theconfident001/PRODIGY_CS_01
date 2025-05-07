def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Leave non-alphabet characters unchanged
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption & Decryption")
    
    # Prompt the user to select encryption or decryption
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    # Check if the input is valid
    if choice not in ['e', 'd']:
        print("Invalid choice, Please enter 'e' or 'd'.")
        return

    # Take the message input from the user
    text = input("Enter the message: ")
    
    # Try to convert the shift value to an integer
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    # Based on the user's choice, either encrypt or decrypt
    if choice == 'e':
        encrypted = caesar_cipher_encrypt(text, shift)
        print("Encrypted message:", encrypted)
    else:
        decrypted = caesar_cipher_decrypt(text, shift)
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
