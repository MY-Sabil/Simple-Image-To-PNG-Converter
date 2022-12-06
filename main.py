from tkinter import filedialog
import customtkinter as ctk
from PIL import Image
from pathlib import Path

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("700x500")
app.title("Simple WEBP/JPG/GIF to PNG Converter")
app.iconbitmap("icon.ico")

def UploadFile():
    filename = filedialog.askopenfilenames()
    global filepaths
    filepaths = filename
    for i in range(0, len(filename)):
        img_size = 100
        img = Image.open(filename[i]).resize((img_size, img_size))
        tmp = ctk.CTkImage(img, size=(img_size, img_size))
        label = ctk.CTkLabel(master=app, text="", image=tmp)
        label.image = tmp
        label.pack(side=ctk.LEFT)
    
    convert_btn.configure(state="normal")
    info_press.configure(text="Press the convert button to start ;)")

def ConvertImage():
    info_press.configure(text="Converting....")
    for i in range(0, len(filepaths)):
        tmp_path = Path(filepaths[i])
        destination = tmp_path.with_suffix(".png")
        temp = Image.open(filepaths[i]).convert("RGB")
        temp.save(destination, 'png')
        print("Saved at: ", destination)
    info_press.configure(text="Converted images saved at original destination! :D")


info_press = ctk.CTkLabel(master=app, text="A Simple Image to PNG Converter", font=("Arial Bold", 20))
info_press.pack(pady=(30, 0), side=ctk.TOP)
info_press = ctk.CTkLabel(master=app, text="Made by Muhaiminul Yeamin", font=("Arial", 14))
info_press.pack(side=ctk.TOP)

import_btn = ctk.CTkButton(master=app, text="Import Files", command=UploadFile, font=("Arial", 15))
import_btn.pack(pady=(20, 0))

convert_btn = ctk.CTkButton(master=app, text="Convert to PNG", command=ConvertImage, font=("Arial", 15))
convert_btn.configure(state="disabled")
convert_btn.pack(pady=(10, 30), side=ctk.BOTTOM)

info_press = ctk.CTkLabel(master=app, text="Import some images first :)", font=("Arial", 16))
info_press.pack(side=ctk.BOTTOM)

app.mainloop()