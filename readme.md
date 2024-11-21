# Belastingdienst Dashboard

Dit project is een grafische gebruikersinterface (GUI) voor het beheren en visualiseren van gegevens met betrekking tot formulieren. Het is gebouwd met behulp van Python en de Tkinter-bibliotheek.

## Functionaliteiten

- **Login Systeem**: Beveiligde toegang met gebruikersnaam/wachtwoord authenticatie
- **Dashboard**: Overzicht van belangrijke statistieken en metrics
- **Formulieren Beheer**: Bekijk en beheer formulieren met zoek- en sorteeropties
- **Rapportages**: Bekijk historische gegevens en trends
- **Changelog Systeem**: Houd wijzigingen bij per formulier

## Vereisten

- Python 3.x
- pandas

## Installatie

1. Clone de repository:

   ```
   git clone <repository-url>
   ```

2. Navigeer naar de projectdirectory:

   ```
   cd HHS-LU4-2024
   ```

3. Installeer de vereiste pakketten:
   ```
   pip install -r requirements.txt
   ```

## Gebruik

1. Start de applicatie:

   ```
   python main.py
   ```

2. Log in met de standaard inloggegevens:

   - Gebruikersnaam: `admin`
   - Wachtwoord: `password`

3. Navigeer door de applicatie met behulp van de navigatiebalk bovenaan.

## Projectstructuur

- `main.py`: Hoofdapplicatie en frame management
- `login.py`: Login systeem en authenticatie
- `dashboard.py`: Dashboard weergave en statistieken
- `forms.py`: Formulieren overzicht en beheer
- `form_detail.py`: Detailweergave van individuele formulieren
- `changelog.py`: Systeem voor het bijhouden van wijzigingen
- `reports.py`: Rapportage en analyse functionaliteit
- `components/`: Herbruikbare UI componenten
- `data/`: Data bestanden en rapportages
- `tests/`: Unit tests

## Data Management

- Formuliergegevens worden opgeslagen in CSV-formaat
- Wekelijkse rapportages worden automatisch gegenereerd
- Changelog wordt bijgehouden per formulier

## Testing

Run de unit tests met:

python -m unittest tests.test_application.TestMainApplication
