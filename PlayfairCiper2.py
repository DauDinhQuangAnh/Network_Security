def prepare_key(key):
    key = key.upper().replace(" ", "").replace("J", "I")
    key_unique = ""
    for char in key:
        if char not in key_unique:
            key_unique += char
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in key_unique:
        alphabet = alphabet.replace(char, "")
    return key_unique + alphabet

def create_grid(key):
    grid = [[0]*5 for _ in range(5)]
    index = 0
    for i in range(5):
        for j in range(5):
            grid[i][j] = key[index]
            index += 1
    return grid

def display_grid(grid):
    for row in grid:
        print(" ".join(row))

def find_position(grid, char):
    for i in range(5):
        for j in range(5):
            if grid[i][j] == char:
                return i, j

def encrypt_decrypt_pair(grid, a, b, encrypt=True):
    row_a, col_a = find_position(grid, a)
    row_b, col_b = find_position(grid, b)
    shift = 1 if encrypt else -1
    
    if row_a == row_b:
        col_a = (col_a + shift) % 5
        col_b = (col_b + shift) % 5
    elif col_a == col_b:
        row_a = (row_a + shift) % 5
        row_b = (row_b + shift) % 5
    else:
        col_a, col_b = col_b, col_a
    
    return grid[row_a][col_a], grid[row_b][col_b]

def encrypt_decrypt_message(key, text, encrypt=True):
    key = prepare_key(key)
    grid = create_grid(key)
    text = text.upper().replace(" ", "").replace("J", "I")
    processed_text = ""
    
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        processed_a, processed_b = encrypt_decrypt_pair(grid, a, b, encrypt)
        processed_text += processed_a + processed_b

    return processed_text

if __name__ == "__main__":
    key = input("Enter the key: ")
    choice = input("Encrypt or Decrypt? (E/D): ").upper()
    text = input("Enter the text: ")

    key = prepare_key(key)
    grid = create_grid(key)
    print("Playfair Matrix:")
    display_grid(grid)

    if choice == 'E':
        encrypted_text = encrypt_decrypt_message(key, text)
        print("Encrypted Text:", encrypted_text)
    elif choice == 'D':
        decrypted_text = encrypt_decrypt_message(key, text, encrypt=False)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice.")
