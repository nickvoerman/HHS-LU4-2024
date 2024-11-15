import tkinter as tk
from components.navigation import create_navigation_bar

class FormulierenFrame(tk.Frame):
    def __init__(self, container, parent):
        super().__init__(container)
        self.parent = parent
        self.create_frame()

    def create_frame(self):
        create_navigation_bar(self, active_tab="Formulieren", navigate_to=self.parent.navigate_to)

        #paragraph with forms text
        forms_text = tk.Label(self, text="Formulieren", font=("Arial", 14))
        forms_text.pack(pady=20)
       