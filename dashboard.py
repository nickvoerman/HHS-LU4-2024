import tkinter as tk
from components.navigation import create_navigation_bar

class DashboardFrame(tk.Frame):
    def __init__(self, container, parent):
        super().__init__(container)
        self.parent = parent
        self.create_frame()

    def create_frame(self):

        create_navigation_bar(self, active_tab="Dashboard", navigate_to=self.parent.navigate_to)

        #paragraph with dashboard text
        dashboard_text = tk.Label(self, text="dit is het dashboard!", font=("Arial", 14))
        dashboard_text.pack(pady=20)