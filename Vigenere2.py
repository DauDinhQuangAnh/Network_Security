from collections import Counter

def frequency_analysis(segment):
    freqs = Counter(segment)
    most_common = freqs.most_common(1)[0][0]
    key_char = chr(((ord(most_common) - ord('E')) + 26) % 26 + ord('A'))
    return key_char

def decrypt_vigenere(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    
    for i in range(len(ciphertext)):
        decrypted_char = chr(((ord(ciphertext[i]) - ord(key[i % key_length])) + 26) % 26 + ord('A'))
        decrypted_text += decrypted_char
        
    return decrypted_text

# Given ciphertext
ciphertext = "cv vvobobxy uocmgjg, olgiaqsliioa dynxyu fi axjwdy qgmqdgimpqz uvw jqygcgpemnqhu vqwpgpsgya wltupmw mtag utajqgimpemf khueqjbl hpp u axa qr lcel-dmmmw jcxwcehvuivl jcxfmw hnsizbajym bh atmhayvty gmlzcsya bu ymsa mocf uzx ocdx bh kgocxalt. fbmll fqnmktkzcampe mfohykfbul htq oaxk hal kkfrfiokhrtck dla syvxycfcwg hpp xqzpvmf abnpuho tuf hyzbmkoubbvp fi xkvvqwb whvm jzbccos, exi ddielpps iv mog uhbxypqn igk eahnbkgznqts eagunukoubbvpe mcvo ce wzxkkf wikk vduvlhefcwgz czx mfhkx"  # Truncated for brevity

# Assuming key length is 5 for demonstration
key_length = 5

# Divide ciphertext into segments
segments = [[] for _ in range(key_length)]
for i in range(len(ciphertext)):
    segments[i % key_length].append(ciphertext[i])

# Perform frequency analysis to guess key
guessed_key = ""
for segment in segments:
    guessed_key += frequency_analysis(segment)

# Decrypt the message using the guessed key
decrypted_text = decrypt_vigenere(ciphertext, guessed_key)
print("Guessed Key:", guessed_key)
print("Decrypted Text:", decrypted_text)
