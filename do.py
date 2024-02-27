import os
import tkinter as tk
from PIL import Image, ImageTk

class ImageSlideshow(tk.Tk):
    def __init__(self, image_folder, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Image Slideshow")
        self.geometry("800x600")
        self.attributes('-fullscreen', True)
        self.image_folder = image_folder
        self.image_paths = self.get_image_paths()
        if not self.image_paths:
            print(f"No image files found in '{self.image_folder}'.")
            return

        self.current_image_index = 0
        self.display_image()

        self.after(2000, self.change_image)

    def get_image_paths(self):
        if not os.path.exists(self.image_folder):
            print(f"Folder '{self.image_folder}' not found.")
            return []
        image_paths = []
        for filename in os.listdir(self.image_folder):
            if filename.endswith(('.jpg', '.png', '.gif')):
                image_paths.append(os.path.join(self.image_folder, filename))
        return image_paths

    def display_image(self):
        path = self.image_paths[self.current_image_index]
        try:
            image = Image.open(path)
            image = image.resize((800, 600), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            if hasattr(self, 'label'):
                self.label.destroy()
            self.label = tk.Label(self, image=photo)
            self.label.image = photo
            self.label.pack(fill=tk.BOTH, expand=True)
        except Exception as e:
            print(f"Error displaying image: {e}")

    def change_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.display_image()
        self.after(2000, self.change_image)

if __name__ == "__main__":
    # Replace 'path_to_your_folder' with the actual path to your image folder
    image_folder = "./img"
    app = ImageSlideshow(image_folder)
    app.mainloop()
