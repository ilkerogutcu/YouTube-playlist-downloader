import requests
import re
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import messagebox,filedialog
from pytube import YouTube,Playlist

root = tk.Tk()
root.geometry("550x110")
root.title("Youtube Playlist Downloader")
root.resizable(False, False)
root.config(background="brown2")

def Ayarlar():
    linkYeri = Label(root, text="PlayList linki giriniz : ", bg="white")
    linkYeri.grid(row=1, column=0, pady=5, padx=5)

    root.linkYaz = Entry(root, width=70)
    root.linkYaz.grid(row=1, column=1, pady=5, padx=5, columnspan = 2)

    hedefYeri = Label(root, text="Kayıt yeri : ", bg="white")
    hedefYeri.grid(row=2, column=0, pady=5, padx=5)

    root.hedefYazi = Entry(root, width=40)
    root.hedefYazi.grid(row=2, column=1, pady=5, padx=5)

    kayitButonu = Button(root, text="Kayıt yeri seç", command=Kayit, width=20)
    kayitButonu.grid(row=2, column=2, pady=5, padx=5)

    indirmeButonu = Button(root, text="İndir", command=indir, width=40)
    indirmeButonu.grid(row=3, column=1, pady=5, padx=5)
    
def Kayit():
    root.hedefDIR= filedialog.askdirectory(initialdir="C:\Python")
    root.hedefYazi.insert('1', root.hedefDIR)
    
def indir():
    website=root.linkYaz.get()
    r=requests.get(website)
    soup = BeautifulSoup(r.text,"html.parser")
    List = [a['href'] for a in soup.find_all('a', href=True)]
    List = [n for n in List if re.search('watch',n)]
    temiz_list=[]
    for n in List:
        if n not in temiz_list:
            temiz_list.append(n)
    
    temiz_list=['https://www.youtube.com' + n for n in temiz_list]
    
    for link in temiz_list:
        pl=YouTube(link)
        t=pl.streams.filter(only_audio=True).all()
        t[0].download(root.hedefDIR)
        
        
            
    messagebox.showinfo("BAŞARILI", "TÜM ŞARKILAR KAYDEDİLDİ\n")
    
    
    
    
    
    
    
    
Ayarlar()
root.mainloop() 
    