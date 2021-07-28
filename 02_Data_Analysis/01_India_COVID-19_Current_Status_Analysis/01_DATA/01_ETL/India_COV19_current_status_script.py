
# Script to extract & cleanse current status data of COVID-19 in India by states #
# ============================================================================== #

# ------ Start of Program ----- #


import pandas as pd
import datetime

rd = pd.read_json('https://www.mohfw.gov.in/data/datanew.json')

StatesFilter = (rd['state_name'] != '')

rd1 = rd[StatesFilter]

new_cols = [
    'SNo.',
    'State Name',
    'Active Cases (Yesterday)',
    'Positive Cases (Yesterday)',
    'Cured Cases (Yesterday)',
    'Death Cases (Yesterday)',
    'Active Cases (Today)',
    'Positive Cases (Today)',
    'Cured Cases (Today)',
    'Death Cases (Today)',
    'StateCode'
]


rd1.columns = new_cols

reordered_cols = [
    'SNo.',
    'StateCode',
    'State Name',
    'Active Cases (Yesterday)',
    'Positive Cases (Yesterday)',
    'Cured Cases (Yesterday)',
    'Death Cases (Yesterday)',
    'Active Cases (Today)',
    'Positive Cases (Today)',
    'Cured Cases (Today)',
    'Death Cases (Today)'
]

rd2 = rd1.reindex(columns = reordered_cols)

rd3 = rd2.set_index('SNo.')

# Adding current date time to show a last-updated column:

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime('%d/%m/%Y %H:%M:%S')

rd3['Last Updated (UTC)'] = formatted_datetime

cd = rd3.sort_index()

# Dumping data into a csv file:

cd.to_csv('../02_FLATFILE/India_COV19_Current_Status.csv', index=True)

# ------ End of Program ----- #