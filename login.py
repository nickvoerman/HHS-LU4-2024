import tkinter as tk
from tkinter import messagebox
from dashboard import open_dashboard

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Belastingdienst Login")
        self.root.geometry("300x200")

        # Login UI
        tk.Label(self.root, text="Inloggen", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Gebruikersnaam:").pack()
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack()

        tk.Label(self.root, text="Wachtwoord:").pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        tk.Button(self.root, text="Login", command=self.verify_login).pack(pady=10)

    def verify_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Simpele verificatie met vaste gebruikersnaam en wachtwoord
        if username == "admin" and password == "password":
            self.root.withdraw()  # Verberg het inlogvenster
            open_dashboard(self.root)  # Open het dashboardvenster
        else:
            messagebox.showerror("Fout", "Onjuiste gebruikersnaam of wachtwoord.")
