# ------------------------- IMPORTS -----------------------------------------------------------------------------------------

import tkinter as tk 
from tkinter import ttk
import json

# ---------------------------------------------------------------------------------------------------------------------------
# ----------------------- DECLARACIÓ TKINTER --------------------------------------------------------------------------------
root = tk.Tk()
root.title("Gestor Hospital Blanes")
# ---------------------------------------------------------------------------------------------------------------------------
# -------------------------- VARIABLES --------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------------
# --------------------------- FUNCIONS --------------------------------------------------------------------------------------
#                                                                                               COMPROVACIÓ LOGIN V
def try_login():
    num = entry_numEmpleat.get()
    passwd = entry_contrasenya.get()
    print(num)
    print(passwd)
    label_textIncorrecte = tk.Label(frame_login,text="", font=("Arial", 10, "bold"), foreground="Red")
    label_textIncorrecte.grid(row=3, column=1)
    label_textIncorrecte.config(text="")
    with open("users.json", "r") as json_users:
        users = json.load(json_users)

    for user in users["users"]:
        if user["id"] == num  and user["password"] == passwd:
            label_textIncorrecte.config(text="!!! Contrasenya o Num. Empleat Correcte !!!")
            return
        else:
            label_textIncorrecte.config(text="!!! Contrasenya o Num. Empleat Incorrecte !!!")



#                                                                                               COMPROVACIÓ LOGIN ∧   
        





# ---------------------------------------------------------------------------------------------------------------------------
# ----------------------- DECLARACIÓ TKINTER --------------------------------------------------------------------------------
tk.Label(root, text="Inicia Sessió", font=("Arial",20, "bold")).pack(side="top", fill="x")
#                                                                                               FRAME DE LOGIN V
frame_login= tk.Frame(root)
frame_login.columnconfigure(0, weight=1)
frame_login.columnconfigure(1, weight=1)
frame_login.rowconfigure(0, weight=1)
frame_login.rowconfigure(1, weight=1)
frame_login.rowconfigure(2, weight=1)
frame_login.rowconfigure(3, weight=1)
frame_login.pack()
#                                                                                               FRAME DE LOGIN ∧

tk.Label(frame_login, text="Num. d'empleat: ",font=("Arial",12, "bold")). grid(row=1, column=0)  # ENTRADA NUMERO D'EMPLEAT
entry_numEmpleat = tk.Entry(frame_login)
entry_numEmpleat.grid(row=1, column= 1)

tk.Label(frame_login, text="Contrasenya: ",font=("Arial",12, "bold")). grid(row=2, column=0)   # ENTRADA CONTRASENYA
entry_contrasenya = tk.Entry(frame_login)
entry_contrasenya.grid(row=2, column= 1)

button_login = tk.Button(frame_login, text="Acceptar", command=try_login)
button_login.grid(row=4, column=1)

# ---------------------------------------------------------------------------------------------------------------------------


root.mainloop()
