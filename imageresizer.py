import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image


def resize_image(input_path, output_path, size):
    try:
        with Image.open(input_path) as img:
        
            img = img.resize(size, Image.ANTIALIAS)
            
            img.save(output_path)
            messagebox.showinfo("Success", f"Image resized and saved at {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error resizing image: {e}")


def open_image():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
    if filepath:
        entry_image_path.delete(0, tk.END)
        entry_image_path.insert(0, filepath)


def on_resize():
    input_path = entry_image_path.get()
    output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
    if input_path and output_path:
        try:
            width = int(entry_width.get())
            height = int(entry_height.get())
            size = (width, height)
            resize_image(input_path, output_path, size)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for width and height.")


root = tk.Tk()
root.title("Image Resizer")


frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=20, pady=20)


label_image_path = tk.Label(frame, text="Select Image:")
label_image_path.grid(row=0, column=0, padx=5, pady=5)

entry_image_path = tk.Entry(frame, width=40)
entry_image_path.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(frame, text="Browse", command=open_image)
button_browse.grid(row=0, column=2, padx=5, pady=5)


label_width = tk.Label(frame, text="Width:")
label_width.grid(row=1, column=0, padx=5, pady=5)

entry_width = tk.Entry(frame, width=10)
entry_width.grid(row=1, column=1, padx=5, pady=5)

label_height = tk.Label(frame, text="Height:")
label_height.grid(row=2, column=0, padx=5, pady=5)

entry_height = tk.Entry(frame, width=10)
entry_height.grid(row=2, column=1, padx=5, pady=5)


button_resize = tk.Button(frame, text="Resize Image", command=on_resize)
button_resize.grid(row=3, column=0, columnspan=3, pady=10)


root.mainloop()
