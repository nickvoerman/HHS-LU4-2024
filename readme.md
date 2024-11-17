# Belastingdienst Dashboard

Dit project is een grafische gebruikersinterface (GUI) voor het beheren en visualiseren van gegevens met betrekking tot formulieren. Het is gebouwd met behulp van Python en de Tkinter-bibliotheek.

## Inhoud

- **MainApplication**: De hoofdklasse die de applicatie beheert en de verschillende frames (schermen) beheert.
- **LoginFrame**: Het inlogscherm waar gebruikers hun inloggegevens kunnen invoeren.
- **DashboardFrame**: Het dashboard dat statistieken en gegevens over formulieren toont.
- **FormulierenFrame**: Een scherm voor het beheren en bekijken van formulieren.
- **Navigatie**: Een navigatiebalk die gebruikers in staat stelt om tussen verschillende secties van de applicatie te navigeren.

## Installatie

1. Zorg ervoor dat je Python 3.x op je systeem hebt geïnstalleerd.
2. Clone dit repository naar je lokale machine:
   ```
   git clone <repository-url>
   ```
3. Navigeer naar de projectdirectory:
   ```
   cd HHS-LU4-2024
   ```
4. Installeer de vereiste pakketten:
   ```
   pip install -r requirements.txt
   ```

## Gebruik

1. Start de applicatie door het volgende commando uit te voeren:
   ```
   python main.py
   ```
2. Voer de standaard inloggegevens in:
   - Gebruikersnaam: `admin`
   - Wachtwoord: `password`
3. Navigeer door de verschillende secties van de applicatie met behulp van de navigatiebalk.

## Bestanden

- `main.py`: De hoofdingang van de applicatie.
- `login.py`: Bevat de inlogfunctionaliteit.
- `dashboard.py`: Bevat de logica voor het dashboard.
- `forms.py`: Bevat de logica voor het beheren van formulieren.
- `components/navigation.py`: Bevat de navigatiebalkcomponent.

## Licentie

Dit project is gelicentieerd onder de MIT-licentie.
