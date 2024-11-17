import tkinter as tk
import pandas as pd
from components.navigation import create_navigation_bar

class DashboardFrame(tk.Frame):
    def __init__(self, container, parent):
        super().__init__(container)
        self.parent = parent
        self.data = self.load_data()  # Laad de gegevens
        self.create_frame()

    def load_data(self):
        # Laad gegevens uit CSV-bestand met pandas
        try:
            df = pd.read_csv('data/forms_data.csv')  # Zorg dat het bestand op de juiste plek staat
            return df
        except FileNotFoundError:
            # Als het bestand niet gevonden wordt, maak een lege dataset aan
            return pd.DataFrame({
                'Bounce_Rate': [0],
                'Fouten': [0],
                'Status': []
            })


    def create_frame(self):
        create_navigation_bar(self, active_tab="Dashboard", navigate_to=self.parent.navigate_to)

    # Paragraaf met dashboard tekst
        dashboard_text = tk.Label(self, text="Dashboard overzicht Scherm", font=("Arial", 16, "bold"))
        dashboard_text.pack(pady=20)

        # Algemene statistieken frame
        general_stats_frame = tk.Frame(self)
        general_stats_frame.pack(pady=10)

        # Labels voor algemene statistieken met zwarte rand en padding
        tk.Label(general_stats_frame, text="Algemene statistieken", font=("Arial", 14, "bold")).grid(row=0, columnspan=3)

        # Aantal formulieren
        self.create_stat_card(general_stats_frame, "Aantal formulieren: " + str(len(self.data)), 1, 0)
        # Bounce rate
        self.create_stat_card(general_stats_frame, "Bounce rate: " + str(round(self.data['Bounce_Rate'].mean(), 2)), 1, 1)
        # Aantal foutmeldingen
        self.create_stat_card(general_stats_frame, "Aantal foutmeldingen: " + str(self.data['Fouten'].sum()), 1, 2)

        # Statussen frame
        status_frame = tk.Frame(self)
        status_frame.pack(pady=10)

        # Labels voor statussen met zwarte rand en padding
        tk.Label(status_frame, text="Statussen", font=("Arial", 14, "bold")).grid(row=0, columnspan=3)

        # Live formulieren
        self.create_stat_card(status_frame, f"{len(self.data[self.data['Status'] == 'Live'])} formulieren live", 1, 0)
        # Afgekeurde formulieren
        self.create_stat_card(status_frame, f"{len(self.data[self.data['Status'] == 'Afgekeurd'])} formulieren afgekeurd", 1, 1)
        # Formulieren in bewerking
        self.create_stat_card(status_frame, f"{len(self.data[self.data['Status'] == 'In bewerking'])} formulieren in bewerking", 1, 2)

    # Create a stat card
    def create_stat_card(self, parent, text, row, column):
        card = tk.Frame(parent, borderwidth=2, relief="solid", padx=10, pady=10)
        card.grid(row=row, column=column, padx=10, pady=10)
        tk.Label(card, text=text).pack()
