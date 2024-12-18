import tkinter as tk
from dashboard import DashboardFrame

class LoginFrame(tk.Frame):
    def __init__(self, container, parent):
        super().__init__(container)
        self.parent = parent

        # Login UI
        tk.Label(self, text="Inloggen", font=("Arial", 16, "bold")).pack(pady=10)

        # Label voor foutmeldingen
        self.error_label = tk.Label(self, text="", fg="red", font=("Arial", 10))
        self.error_label.pack()

        # Username label and entry
        tk.Label(self, text="Gebruikersnaam:").pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()
        self.entry_username.focus()

        # Password label and entry
        tk.Label(self, text="Wachtwoord:").pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()
        
        # Login button
        tk.Button(self, text="Login", command=self.verify_login).pack(pady=10)
        
    def verify_login(self):
        # Get username and password
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Simple verification with fixed username and password
        if username == "admin" and password == "password":

            # Clear the entry fields and remove focus 
            self.entry_username.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)

            # Focus first field
            self.entry_username.focus()

            # Switch to the dashboard frame
            self.parent.switch_frame(DashboardFrame)  
            
            #hide error message when login is successful
            self.error_label.config(text="")
            
        else:
            self.show_error("Onjuiste gebruikersnaam of wachtwoord.")

    # Show error message in error_label
    def show_error(self, message):
        self.error_label.config(text=message)