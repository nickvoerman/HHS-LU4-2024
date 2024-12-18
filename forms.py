import tkinter as tk
import pandas as pd
from components.navigation import create_navigation_bar
from changelog import ChangelogFrame
from form_detail import FormDetailFrame
from tkinter import messagebox

class FormulierenFrame(tk.Frame):
    def __init__(self, container, parent):
        super().__init__(container)
        self.container = container
        self.parent = parent
        
        # Load data from CSV
        self.data = self.load_data()  
        
        # Variable to track sorting order
        self.is_sorted_ascending = True  
        
        # Create the frame layout
        self.create_frame()  

    def load_data(self):
        try:
            # Ensure the file is in the correct location
            df = pd.read_csv('data/forms.csv')  
            return df 
        except FileNotFoundError:
            # Return empty DataFrame if file not found
            return pd.DataFrame({
                'Naam': [],
                'Formulier_ID': []
            })

    def create_frame(self):
        # Create navigation bar
        create_navigation_bar(self, active_tab="Formulieren", navigate_to=self.parent.navigate_to)  

        # Title label
        title_text = tk.Label(self, text="Formulieren overzicht scherm", font=("Arial", 16, "bold"))  
        title_text.pack(pady=20) 

        # Create filter frame
        filter_frame = tk.Frame(self)  
        filter_frame.pack(pady=10) 

        # Filter label
        filter_label = tk.Label(filter_frame, text="Filter A-Z", cursor="hand2", font=("Arial", 12))  
        filter_label.pack(side="left", pady=10, padx=(10, 0))  
        
        # Bind click event to toggle sort order
        filter_label.bind("<Button-1>", self.toggle_sort_order)  

        # Variable to hold the filter text
        self.filter_var = tk.StringVar()  
        
        # Filter entry field
        filter_entry = tk.Entry(filter_frame, textvariable=self.filter_var)  
        filter_entry.pack(side="left", pady=5, padx=(20, 10))  
        
        # Bind key release event to update filter
        filter_entry.bind("<KeyRelease>", self.update_filter)  

        # Create a frame to hold the canvas and scrollbar
        outer_frame = tk.Frame(self, borderwidth=2, relief="solid", bg="black")  
        outer_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Create a canvas for scrolling
        self.canvas = tk.Canvas(outer_frame)  
        self.scrollable_frame = tk.Frame(self.canvas)  

        # Vertical scrollbar
        scrollbar = tk.Scrollbar(outer_frame, orient="vertical", command=self.canvas.yview)  
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create window in canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")  

        # Update the scroll region
        def on_configure(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        # Bind configure event to update scroll region
        self.scrollable_frame.bind("<Configure>", on_configure)  

        # Populate the forms initially
        self.populate_forms()  

    def populate_forms(self):
        # Display all forms initially
        self.display_forms(self.data)  

    def display_forms(self, data):
        # Clear the current displayed forms
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()  
        
        # Create a new row for each form
        for index, row in data.iterrows():
            self.create_form_row(row)  

    def update_filter(self, event):
        # Get the current filter text
        filter_text = self.filter_var.get().lower()  
        
        # Filter data
        filtered_data = self.data[self.data['Naam'].str.lower().str.contains(filter_text)]  
        
        # Display filtered forms
        self.display_forms(filtered_data)  

    def toggle_sort_order(self, event):
        # Toggle sort order
        self.is_sorted_ascending = not self.is_sorted_ascending  
        
        # Sort data
        sorted_data = self.data.sort_values(by='Naam', ascending=self.is_sorted_ascending)  
        
        # Display sorted forms
        self.display_forms(sorted_data)  

    def create_form_row(self, row):
        # Get form name and ID
        form_name = row['Naam']
        form_id = row['Formulier_ID']

        # Create form row
        form_row = tk.Frame(self.scrollable_frame, borderwidth=1, relief="solid")
        form_row.pack(pady=5, fill="x", padx=10)

        # Create label frame
        label_frame = tk.Frame(form_row)
        label_frame.pack(side="left", fill="x", expand=True)

        # Label for form name
        tk.Label(label_frame, text=form_name, width=30).pack(side="left", padx=5)
        
        # Label for form ID
        tk.Label(label_frame, text=form_id, width=10).pack(side="left", padx=5)

        # Create buttons frame for better organization
        buttons_frame = tk.Frame(form_row)
        buttons_frame.pack(side="right")

        # Delete button (new)
        delete_button = tk.Button(
            buttons_frame, 
            text="Delete", 
            fg="red",
            command=lambda: self.delete_form(form_id)
        )
        delete_button.pack(side="right", padx=5)

        # Existing buttons
        changelog_button = tk.Button(
            buttons_frame, 
            text="Changelog", 
            command=lambda: self.open_changelog(form_id)
        )
        changelog_button.pack(side="right", padx=5)

        view_button = tk.Button(
            buttons_frame, 
            text="View", 
            command=lambda: self.open_form_detail(form_id)
        )
        view_button.pack(side="right", padx=5)

    # Open changelog frame
    def open_changelog(self, form_id):
        # Create changelog frame with the correct form_id
        changelog_frame = ChangelogFrame(self.container, self.parent, form_id)
        
        # Update the frame with the new changelog frame class
        self.parent.update_frame(ChangelogFrame, changelog_frame)  # Pass the class, not the instance
        
        # Switch to the ChangelogFrame
        self.parent.switch_frame(changelog_frame.__class__)  

    # Open form detail frame
    def open_form_detail(self, form_id):
        # Create form detail frame with the correct form_id
        form_detail_frame = FormDetailFrame(self.container, self.parent, form_id)
        
        # Update the frame with the new form detail frame class
        self.parent.update_frame(FormDetailFrame, form_detail_frame)
        
        # Switch to the FormDetailFrame
        self.parent.switch_frame(form_detail_frame.__class__)

    def delete_form(self, form_id):
        # Show confirmation dialog
        confirm = tk.messagebox.askyesno(
            "Bevestig verwijdering",
            f"Weet je zeker dat je formulier {form_id} wilt verwijderen?"
        )
        
        if confirm:
            try:
                # Read the current CSV file
                df = pd.read_csv('data/forms.csv')
                
                # Remove the row with the matching form_id
                df = df[df['Formulier_ID'] != form_id]
                
                # Save the updated DataFrame back to CSV
                df.to_csv('data/forms.csv', index=False)
                
                # Update the class's data attribute
                self.data = df
                
                # Refresh the display
                self.display_forms(self.data)
                
                # Show success message
                tk.messagebox.showinfo(
                    "Succes",
                    f"Formulier {form_id} is succesvol verwijderd."
                )
                
            except Exception as e:
                # Show error message if something goes wrong
                tk.messagebox.showerror(
                    "Fout",
                    f"Er is een fout opgetreden bij het verwijderen van het formulier: {str(e)}"
                )