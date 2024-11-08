import tkinter as tk

def open_dashboard(root):
    # Maak een nieuw venster voor het dashboard
    dashboard_window = tk.Toplevel(root)
    dashboard_window.title("Dashboard")
    dashboard_window.geometry("300x200")

    # Dashboard inhoud
    tk.Label(dashboard_window, text="Je bent ingelogd", font=("Arial", 14)).pack(pady=50)

    # Sluitknop voor het dashboard
    tk.Button(dashboard_window, text="Afsluiten", command=root.quit).pack(pady=10)
