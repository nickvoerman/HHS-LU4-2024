import tkinter as tk

def create_navigation_bar(root, active_tab, navigate_to=None):
    # Create a frame for the navigation bar
    tab_frame = tk.Frame(root)
    tab_frame.pack(pady=10, fill="x")

    # List of tabs to display in the navigation bar
    tabs = ["Dashboard", "Formulieren", "Rapportages"]
    for tab in tabs:
        # Set the color of the tab based on whether it is active
        color = "blue" if tab == active_tab else "black"
        # Create a label for each tab
        tab_label = tk.Label(tab_frame, text=tab, font=("Arial", 10), fg=color, cursor="hand2", padx=5)
        # Pack the tab label to the left side of the navigation bar
        tab_label.pack(side="left", padx=10)
        # Bind a click event to each tab label to navigate to the corresponding tab
        tab_label.bind("<Button-1>", lambda e, tab=tab: navigate_to(tab) if navigate_to else None)

    # Create a logout button
    logout_button = tk.Button(tab_frame, text="Logout", fg="red", font=("Arial", 10))
    # Bind a click event to the logout button to navigate to the Login tab
    logout_button.bind("<Button-1>", lambda e: navigate_to("Login"))
    # Pack the logout button to the right side of the navigation bar
    logout_button.pack(side="right", padx=10)

    return tab_frame