def encrypt(text, key):
    shift = key % 26
    encrypted_text = ""
    
    for char in text:
        base = ord('a') if char.islower() else ord('A')
        if char.isalpha():
            char = chr(((ord(char) - base + shift) % 26) + base)
        encrypted_text += char
        
    return encrypted_text

def decrypt(text, key):
    return encrypt(text, -key)

def brute_force(ciphertext):
    for key in range(26):
        print(f"Key={key}: {decrypt(ciphertext, key)}")

def main():
    choices = {
        '1': ("Encrypt", lambda: encrypt(input("Enter plaintext: "), int(input("Enter key: ")))),
        '2': ("Decrypt", lambda: decrypt(input("Enter ciphertext: "), int(input("Enter key: ")))),
        '3': ("Brute-force", lambda: brute_force(input("Enter ciphertext: ")))
    }
    
    while True:
        print("\nCaesar Cipher")
        for k, (label, _) in choices.items():
            print(f"{k}. {label}")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '4':
            print("Exiting...")
            break
            
        action = choices.get(choice, None)
        if action:
            print(f"{action[0]}ed: {action[1]()}") 
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
