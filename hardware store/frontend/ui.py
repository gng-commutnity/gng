import customtkinter as ctk
from PIL import Image

def launch():
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("My App")
    root.geometry("600x400")

    label = ctk.CTkLabel(root, text="Hello, CustomTkinter")
    label.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    launch()
