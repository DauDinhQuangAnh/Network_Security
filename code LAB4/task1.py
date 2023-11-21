import hashlib
import tkinter as tk
from tkinter import filedialog

def calculate_hash(input_data, hash_type):
    if hash_type not in ["md5", "sha1", "sha256"]:
        return None

    hash_obj = hashlib.new(hash_type)
    
    if isinstance(input_data, str):
        hash_obj.update(input_data.encode())
    elif isinstance(input_data, bytes):
        hash_obj.update(input_data)
    else:
        return None

    return hash_obj.hexdigest()

def calculate_hash_file(file_path, hash_type):
    if hash_type not in ["md5", "sha1", "sha256"]:
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

def calculate_hash_values():
    input_data = input_text.get()
    hash_type = hash_option.get()

    if hash_type == "File":
        file_path = filedialog.askopenfilename()
        if file_path:
            hash_value = calculate_hash_file(file_path, hash_option_file.get())
    else:
        hash_value = calculate_hash(input_data, hash_type)
    
    if hash_value:
        result_text.delete(1.0, tk.END)  # Clear the previous result
        result_text.insert(tk.END, hash_value)

app = tk.Tk()
app.title("Hash Calculator")

hash_option = tk.StringVar(value="md5")
hash_option_file = tk.StringVar(value="md5")

input_label = tk.Label(app, text="Input Text, Hex String, or Select File:")
input_label.pack()

input_text = tk.Entry(app)
input_text.pack()

file_button = tk.Radiobutton(app, text="File", variable=hash_option, value="File")
file_button.pack()

hash_type_label = tk.Label(app, text="Select Hash Type:")
hash_type_label.pack()

hash_options = ["md5", "sha1", "sha256"]
hash_type_menu = tk.OptionMenu(app, hash_option, *hash_options)
hash_type_menu.pack()

hash_type_menu_file = tk.OptionMenu(app, hash_option_file, *hash_options)
hash_type_menu_file.pack()

calculate_button = tk.Button(app, text="Calculate", command=calculate_hash_values)
calculate_button.pack()

result_label = tk.Label(app, text="Result:")
result_label.pack()

result_text = tk.Text(app, height=2, width=40)
result_text.pack()

app.mainloop()
