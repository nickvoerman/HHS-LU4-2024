import tkinter as tk
import pandas as pd
from components.navigation import create_navigation_bar

class ReportFrame(tk.Frame):
    def __init__(self, container, parent):
        super().__init__(container)
        self.parent = parent
        self.data = self.load_data()
        self.create_frame()

    def load_data(self):
        # Load data from CSV file using pandas
        try:
            df = pd.read_csv('data/form_reports.csv') 
            return df
        except FileNotFoundError:
            # If the file is not found, create an empty dataset
            return pd.DataFrame({
                'Report_Date': [],
                'Total_Forms': [],
                'Average_Bounce_Rate': [],
                'Total_Errors': []
            })

    def create_frame(self):
        create_navigation_bar(self, active_tab="Reports", navigate_to=self.parent.navigate_to)

        # Paragraph with dashboard text
        report_text = tk.Label(self, text="Rapportages overzichtscherm", font=("Arial", 16, "bold"))
        report_text.pack(pady=20)

        # Show the reports
        self.display_reports()
        
    def display_reports(self):
        # Create labels for each row in the loaded data
        for index, row in self.data.iterrows():
            report_label = tk.Label(
                self,
                text=f"Datum: {row['Report_Date']}, Aantal formulieren: {row['Total_Forms']}, Gemiddelde bounce rate: {row['Average_Bounce_Rate']}, Aantal fouten: {row['Total_Errors']}",
                font=("Arial", 12),
                borderwidth=2,
                relief="solid",
                padx=10,
                pady=10
            )
            report_label.pack(pady=5, padx=10)
