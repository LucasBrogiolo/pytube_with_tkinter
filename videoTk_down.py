import tkinter as tk
from tkinter.constants import BOTTOM, TOP
from pytube import YouTube
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x500")
root.title("YouTube video downloader")

label_head = tk.Label(root, text="### YOUTUBE DOWNLOADER ###\n\n\n\n\n\n")
label_head.pack(side=TOP)

# create a input text:
label_link = tk.Label(root, text="Enter YT link:")
label_link.pack()
link_yt = tk.Entry(root)
link_yt.insert(0, "")
link_yt.pack()

# create a  second input text:
label_name = tk.Label(root, text="Enter file name:")
label_name.pack()
name_file = tk.Entry(root)
name_file.insert(0, "")
name_file.pack()

def onClick():
    link = str(link_yt.get())
    name = str(name_file.get())        
    try:
        yt = YouTube(link)
    except:
        messagebox.showerror("Alert", "Conection Error")
        
    video = yt.streams.filter(file_extension="mp4", res="720p").first()

    try:
        video.download("/Users/Documents/videosYT/", f"{name}.mp4")
        messagebox.showinfo("Succes", "Video File created at: Documents/videosYT")
        
    except:
        messagebox.showerror("Alert", "Houve algum erro")

botao = tk.Button(root, text="** Download your video **", command=onClick)
botao.pack()

label_bottom = tk.Label(root, text="\n\n\n### THANKS FOR USE ###\nby: Lucas Brogiolo\nPercussivoBR")
label_bottom.pack(side=BOTTOM)

root.mainloop()
