import tkinter
import customtkinter as ctk
from bs4 import BeautifulSoup
from tkinter.ttk import *
from tkinter import *

i = 0
m = 5

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

login = ctk.CTk()
login.geometry("500x350")
login.minsize(500, 350)
login.maxsize(500, 350)
login.title("Brute-Force")




def action():
    id = champ1.get()
    mdp = champ2.get()

    if id == '789':
        i = 1
    else:
        i = 0

    if mdp == '123':
        m = 1
    else:
        m = 5

    if i == m :
        bf = ctk.CTk()
        login.destroy()
        bf.geometry("500x400")
        bf.minsize(500, 400)
        bf.maxsize(500, 400)
        bf.title("Brute-Force")
        print('enfin')

        frame2 = ctk.CTkFrame(master=bf)
        frame2.pack(pady=20, padx=60, fill="both", expand=True)


        bfr2 = Button(bf,text="Brute-Force", width=42, command=action2)
        bfr2.pack()
        bfr2.place(x=80, y=30)

        bfr3 = Button(bf,text="Autre-1", width=42 )
        bfr3.pack()
        bfr3.place(x=80, y=80)


        bfr4 = Button(bf,text="Autre-2", width=42 )
        bfr4.pack()
        bfr4.place(x=80, y=130)


        bfr5 = Button(bf,text="Autre-3", width=42 )
        bfr5.pack()
        bfr5.place(x=80, y=180)



        bf.mainloop()
    else:
        print("tfq ?")



frame = ctk.CTkFrame(master=login)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Se connecter")
label.pack(pady=12,padx=10)

champ1 = ctk.CTkEntry(master=frame, placeholder_text="Identifiant")
champ1.pack(pady=12)

champ2 = ctk.CTkEntry(master=frame, placeholder_text="Mots de passe", show="*")
champ2.pack(pady=12)

boutton = ctk.CTkButton(master=frame, text="connexion", command=action)
boutton.pack(pady=12,padx=10)

login.mainloop()
