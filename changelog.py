import tkinter as tk
from components.navigation import create_navigation_bar

class ChangelogFrame(tk.Frame):
    def __init__(self, container, parent, form_id=None):
        super().__init__(container)
        self.parent = parent
        self.container = container
        self.form_id = form_id
        
        # Call create_frame with a timeout of 100 milliseconds. This to fix a bug where the frame is not updated correctly.
        self.after(100, self.create_frame)  

    def create_frame(self):
        create_navigation_bar(self, active_tab="Changelog", navigate_to=self.parent.navigate_to)
        
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
                f.write(f"\n{self.form_id},{changelog_text}")
            self.changelog_entry.delete(0, tk.END)  # Maak het invoerveld leeg
            
            # Open form detail frame
            self.open_form_detail(self.form_id)
            
    # Open form detail frame
    def open_form_detail(self, form_id):
        from form_detail import FormDetailFrame
        
        # Create form detail frame with the correct form_id
        form_detail_frame = FormDetailFrame(self.container, self.parent, form_id)
        
        # Update the frame with the new form detail frame class
        self.parent.update_frame(FormDetailFrame, form_detail_frame)
        
        # Switch to the FormDetailFrame
        self.parent.switch_frame(form_detail_frame.__class__)