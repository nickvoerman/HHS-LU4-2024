import tkinter as tk
import pandas as pd
from components.navigation import create_navigation_bar

class FormDetailFrame(tk.Frame):
    def __init__(self, container, parent, form_id=None):
        super().__init__(container)
        self.parent = parent
        self.form_id = form_id
        
        #return nothing if there is no form_id
        if self.form_id is None:
            return
        
        self.container = container
        
        # Load form data and changelog
        self.form_data = self.load_form_data()
        self.changelog_data = self.load_changelog_data()
        
        # Call create_frame with a timeout of 100 milliseconds to fix a bug where the frame is not updated correctly.
        self.after(100, self.create_frame)  

    def load_form_data(self):
        try:
            df = pd.read_csv('data/forms.csv')
            return df[df['Formulier_ID'] == self.form_id].iloc[0]  # Get the row for the specific form_id
        except Exception as e:
            print(f"Error loading form data: {e}")
            return None

    def load_changelog_data(self):
        try:
            df = pd.read_csv('data/changelog.csv')
            return df[df['form_id'] == self.form_id]  # Filter changelog by form_id
        except Exception as e:
            print(f"Error loading changelog data: {e}")
            return pd.DataFrame()  # Return empty DataFrame if there's an error

    def create_frame(self):

        create_navigation_bar(self, active_tab="Formulier details", navigate_to=self.parent.navigate_to)
        
         # Titel
        title_text = tk.Label(self, text=f"{self.form_data['Naam']} - {self.form_id}", font=("Arial", 16, "bold"))
        title_text.pack(pady=10)

        # Formulier Statistieken
        stats_frame = tk.Frame(self)
        stats_frame.pack(pady=10)
        
        # Vierkante blokken voor statistieken
        for label, value in [
            ("Status", self.form_data['Status']),
            ("Bounce rate", self.form_data['Bounce_Rate']),
            ("Aantal foutmeldingen", self.form_data['Fouten'])
        ]:
            stat_block = tk.Frame(stats_frame, bd=2, relief="solid", width=150, height=50)
            stat_block.pack_propagate(False)
            stat_block.pack(side="left", padx=10)
            tk.Label(stat_block, text=label, font=("Arial", 12, "bold")).pack()
            tk.Label(stat_block, text=value, font=("Arial", 12)).pack()

        # Changelog sectie
        changelog_title = tk.Label(self, text="Changelog", font=("Arial", 16, "bold"))
        changelog_title.pack(pady=10)

        changelog_frame = tk.Frame(self, padx=10, pady=10)
        changelog_frame.pack(fill="x", padx=10)

        for _, row in self.changelog_data.iterrows():
            # Create a separate frame for each changelog item
            changelog_item_frame = tk.Frame(changelog_frame, bd=2, relief="solid", padx=5, pady=5)
            changelog_item_frame.pack(fill="x", pady=5)

            # Add the text to the frame
            changelog_item = tk.Label(changelog_item_frame, text=row['changelog'], font=("Arial", 12), anchor="w")
            changelog_item.pack(fill="x")

        # Button for extra field
        changelog_button = tk.Button(self, text="Maak extra veld aan", command=lambda: self.open_changelog(self.form_id))
        changelog_button.pack(pady=10)

    # Open changelog frame
    def open_changelog(self, form_id):
        from changelog import ChangelogFrame
        
        # Create changelog frame with the correct form_id
        changelog_frame = ChangelogFrame(self.container, self.parent, form_id)
        
        # Update the frame with the new changelog frame class
        self.parent.update_frame(ChangelogFrame, changelog_frame)  # Pass the class, not the instance
        
        # Switch to the ChangelogFrame
        self.parent.switch_frame(changelog_frame.__class__)  