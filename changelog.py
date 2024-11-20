import tkinter as tk
from components.navigation import create_navigation_bar

class ChangelogFrame(tk.Frame):
    def __init__(self, container, parent, form_id=None):
        super().__init__(container)
        self.parent = parent
        self.form_id = form_id
        
        # Call create_frame with a timeout of 20 milliseconds. This to fix a bug where the frame is not updated correctly.
        self.after(20, self.create_frame)  

    def create_frame(self):
        create_navigation_bar(self, active_tab="Changelog", navigate_to=self.parent.navigate_to)
        
        #label with only form_id
        form_id_label = tk.Label(self, text=self.form_id, font=("Arial", 12))
        form_id_label.pack(pady=10)

        # Titel
        title_text = tk.Label(self, text=f"Changelog aanmaken voor formulier ID: {self.form_id}", font=("Arial", 16, "bold"))
        title_text.pack(pady=20)

        # Invoerveld voor changelog
        self.changelog_entry = tk.Entry(self, width=50, font=("Arial", 12), background="white")
        self.changelog_entry.pack(pady=10)

        # Voeg toe knop
        add_button = tk.Button(self, text="Voeg toe", command=self.add_changelog)
        add_button.pack(pady=10)

    def add_changelog(self):
        changelog_text = self.changelog_entry.get()
        if changelog_text:
            # Voeg changelog toe aan CSV
            with open('data/changelog.csv', 'a') as f:
                f.write(f"{self.form_id},{changelog_text}\n")
            self.changelog_entry.delete(0, tk.END)  # Maak het invoerveld leeg
            
            #TODO: go to detail page of form when form detail page is created