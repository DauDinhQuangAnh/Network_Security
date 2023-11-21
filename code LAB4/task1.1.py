import hashlib
import tkinter as tk
from tkinter import filedialog

def calculate_hash_file(file_path, hash_type):
    if hash_type not in ["md5", "sha1"]:
        return None

    hash_obj = hashlib.new(hash_type)

    try:
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(65536)  # Read in 64k chunks
                if not data:
                    break
                hash_obj.update(data)
    except FileNotFoundError:
        return None

    return hash_obj.hexdigest()

def calculate_hashes():
    original_file_path = filedialog.askopenfilename(title="Select the original file")
    downloaded_file_path = filedialog.askopenfilename(title="Select the downloaded file")

    md5_original_hash = calculate_hash_file(original_file_path, "md5")
    sha1_original_hash = calculate_hash_file(original_file_path, "sha1")

    md5_downloaded_hash = calculate_hash_file(downloaded_file_path, "md5")
    sha1_downloaded_hash = calculate_hash_file(downloaded_file_path, "sha1")

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"MD5 Original: {md5_original_hash}\nSHA-1 Original: {sha1_original_hash}\nMD5 Downloaded: {md5_downloaded_hash}\nSHA-1 Downloaded: {sha1_downloaded_hash}")

app = tk.Tk()
app.title("Hash Comparison")

calculate_button = tk.Button(app, text="Calculate Hashes", command=calculate_hashes)
calculate_button.pack()

result_text = tk.Text(app, height=8, width=40)
result_text.pack()

app.mainloop()
