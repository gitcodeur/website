import customtkinter as ctk

i = 0
m = 0

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

    if id == 'MaFgui':
        i = 1
    else:
        i = 0

    if mdp == '123':
        m = 1
    else:
        m = 0

    if i == m :
        bf = ctk.CTk()
        login.destroy()
        bf.geometry("500x400")
        bf.minsize(500, 400)
        bf.maxsize(500, 400)
        bf.title("Brute-Force")
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
