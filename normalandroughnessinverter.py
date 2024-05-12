import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image

class TextureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Texture Converter")
        self.root.geometry("400x200")

        self.tabControl = ttk.Notebook(root)
        self.tabControl.pack(expand=1, fill="both")

        self.normal_map_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.normal_map_tab, text="Normal Map")
        self.create_normal_map_tab()

        self.roughness_to_specular_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.roughness_to_specular_tab, text="Roughness to Specular")
        self.create_roughness_to_specular_tab()

    def create_normal_map_tab(self):
        self.normal_map_button = tk.Button(self.normal_map_tab, text="Open Normal Map", command=self.open_normal_map)
        self.normal_map_button.pack()

    def create_roughness_to_specular_tab(self):
        self.roughness_button = tk.Button(self.roughness_to_specular_tab, text="Open Roughness Map", command=self.open_roughness_map)
        self.roughness_button.pack()

    def open_normal_map(self):
        file_path = filedialog.askopenfilename(title="Open Normal Map", filetypes=[("Images", "*.png;*.jpg;*.bmp")])
        if file_path:
            image = Image.open(file_path)
            inverted_image = list(image.split())
            inverted_image[1] = inverted_image[1].point(lambda i: 255 - i)
            inverted_image = Image.merge(image.mode, inverted_image)
            self.save_image(inverted_image)

    def open_roughness_map(self):
        file_path = filedialog.askopenfilename(title="Open Roughness Map", filetypes=[("Images", "*.png;*.jpg;*.bmp")])
        if file_path:
            image = Image.open(file_path)
            inverted_image = Image.eval(image, lambda x: 255 - x)
            self.save_image(inverted_image)

    def save_image(self, image):
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            image.save(save_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextureConverter(root)
    root.mainloop()