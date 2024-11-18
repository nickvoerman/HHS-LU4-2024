#This script should be run every week to generate a report of the current state of the forms
import pandas as pd
from datetime import datetime

# Load the data from the forms (Normally loaded from the database)
forms = pd.read_csv('data/forms.csv')

# Calculate the statistics
total_forms = len(forms)
average_bounce_rate = forms['Bounce_Rate'].mean() if 'Bounce_Rate' in forms.columns else 0
total_errors = forms['Fouten'].sum() if 'Fouten' in forms.columns else 0
report_date = datetime.now().strftime("%Y-%m-%d")

# Create a DataFrame for the report
report_data = {
    'Report_Date': [report_date],
    'Total_Forms': [total_forms],
    'Average_Bounce_Rate': [average_bounce_rate],
    'Total_Errors': [total_errors]
}

report_df = pd.DataFrame(report_data)

# Save the report as CSV, append to the existing file
# mode 'a' append to the file, header=false to not add a header if the file already exists
report_df.to_csv('data/form_reports.csv', mode='a', header=not pd.io.common.file_exists('data/form_reports.csv'), index=False)