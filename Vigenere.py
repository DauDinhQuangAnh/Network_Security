def encrypt_decrypt_vigenere(text, key, encrypt=True):
    key_length = len(key)
    key = key.upper()
    text = text.upper().replace(" ", "")
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        key_char = key[i % key_length]
        
        if encrypt:
            encrypted_char = chr(((ord(char) - 65 + ord(key_char) - 65) % 26) + 65)
            result += encrypted_char
        else:
            decrypted_char = chr(((ord(char) - 65 - (ord(key_char) - 65) + 26) % 26) + 65)
            result += decrypted_char
            
    return result

if __name__ == "__main__":
    key = input("Enter the key: ")
    choice = input("Encrypt or Decrypt? (E/D): ").upper()
    text = input("Enter the text: ")
    
    if choice == 'E':
        encrypted_text = encrypt_decrypt_vigenere(text, key)
        print("Encrypted Text:", encrypted_text)
    elif choice == 'D':
        decrypted_text = encrypt_decrypt_vigenere(text, key, encrypt=False)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice.")
