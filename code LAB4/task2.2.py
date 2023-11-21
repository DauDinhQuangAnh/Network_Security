import hashlib

def md5_hash(string):
   hash_object = hashlib.md5(string.encode())
   return hash_object.hexdigest()

string1 = "d1 31 dd 02 c5 e6 ee c4 69 3d 9a 06 98 af f9 5c 2f ca b5 87 12 46 7e ab 40 04 58 3e b8 fb 7f 89 55 ad 34 06 09 f4 b3 02 83 e4 88 83 25 71 41 5a 08 51 25 e8 f7 cd c9 9f d9 1d bd f2 80 37 3c 5b d8 82 3e 31 56 34 8f 5b ae 6d ac d4 36 c9 19 c6 dd 53 e2 b4 87 da 03 fd 02 39 63 06 d2 48 cd a0 e9 9f 33 42 0f 57 7e e8 ce 54 b6 70 80 a8 0d 1e c6 98 21 bc b6 a8 83 93 96 f9 65 2b 6f f7 2a 70"
string2 = "d1 31 dd 02 c5 e6 ee c4 69 3d 9a 06 98 af f9 5c 2f ca b5 07 12 46 7e ab 40 04 58 3e b8 fb 7f 89 55 ad 34 06 09 f4 b3 02 83 e4 888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70"

hash1 = md5_hash(string1)
hash2 = md5_hash(string2)

print(f"Giá trị băm MD5 cho chuỗi 1 là: {hash1}")
print(f"Giá trị băm MD5 cho chuỗi 2 là: {hash2}")
