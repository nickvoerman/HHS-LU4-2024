import tkinter as tk

def create_navigation_bar(root, active_tab, navigate_to=None):
    tab_frame = tk.Frame(root, bd=2, relief="solid", padx=5, pady=5)
    tab_frame.pack(pady=10, fill="x")

    tabs = ["Dashboard", "Formulieren", "Rapportages"]
    for tab in tabs:
        color = "blue" if tab == active_tab else "black"
        tab_label = tk.Label(tab_frame, text=tab, font=("Arial", 10), fg=color, cursor="hand2", padx=5)
        tab_label.pack(side="left", padx=10)

        tab_label.bind("<Button-1>", lambda e, tab=tab: navigate_to(tab) if navigate_to else None)

    logout_button = tk.Button(tab_frame, text="Logout", fg="red", font=("Arial", 10),
                              command=root.quit)
    logout_button.pack(side="right", padx=10)

    return tab_frame