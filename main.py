import tkinter as tk
from login import LoginWindow

# Applicatie starten
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
