def prepare_key(key):
    key = key.replace(" ", "").upper()
    key = "".join(sorted(set(key), key=lambda x: key.find(x)))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in key:
        alphabet = alphabet.replace(char, "")
    return key + alphabet

def create_grid(key):
    grid = [[0]*5 for _ in range(5)]
    index = 0
    for i in range(5):
        for j in range(5):
            grid[i][j] = key[index]
            index += 1
    return grid

def find_position(grid, char):
    for i in range(5):
        for j in range(5):
            if grid[i][j] == char:
                return i, j

def decrypt_pair(grid, a, b):
    row_a, col_a = find_position(grid, a)
    row_b, col_b = find_position(grid, b)
    
    if row_a == row_b:
        col_a = (col_a - 1) % 5
        col_b = (col_b - 1) % 5
    elif col_a == col_b:
        row_a = (row_a - 1) % 5
        row_b = (row_b - 1) % 5
    else:
        col_a, col_b = col_b, col_a
    
    return grid[row_a][col_a], grid[row_b][col_b]

def decrypt_message(key, cipher_text):
    key = prepare_key(key)
    grid = create_grid(key)
    cipher_text = cipher_text.upper().replace(" ", "")
    decrypted_text = ""
    
    for i in range(0, len(cipher_text), 2):
        a, b = cipher_text[i], cipher_text[i+1]
        decrypted_a, decrypted_b = decrypt_pair(grid, a, b)
        decrypted_text += decrypted_a + decrypted_b

    return decrypted_text

key = "Harry Potter"
cipher_text = "ARYWYPHCBVEBYGMPNCYGCNTDNCWTMGRMFTQPLEWTMLREFBEBQEBIYGBFLPHVOAEHKDHEUNGQFEROLEWTMLOPHEQGOSBEROQDWTLCMTHBWLNRKXRYLORYYPHCBVEBYRLGYDMKYGGWKLROANDBWGNERMNGYRLGHEWRTRLMBRHMUDGVODVTEGMCHLGWCMTFODNRRYCMZKODDUTDXGEOPOYRMFRMGUKXRYGHABROVTGQMCEHPRPEOTSEGEQLARYWYPOTMGQDOEXGOAUDHGUTULTNEHFTFHPGXGVPHGURBDMEGWKLETCBOTNTFQLTAEHMTUGEOAHEVEROXGVPHGDEWTEWGQIEDLPILERWPMOATNGQKQEAHBMVRFKBRMKLXODXFREBHMNUKXRYKLRMFLWDDNCN"
decrypted_text = decrypt_message(key, cipher_text)
print("Decrypted Text:", decrypted_text)
