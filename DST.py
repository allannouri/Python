import requests
import pandas as pd
from IPython.display import display
from io import StringIO
from dstapi import DstApi # The helper class

# Directly embed parameters in the URL with response.get()
requests.get('https://api.statbank.dk/v1' + '/tableinfo' + "?id=metrox1&format=JSON").json()

# Pass a dictionary of parameters to requests.get()
params = {'id': 'metrox1', 'format': 'JSON'}
requests.get('https://api.statbank.dk/v1' + '/tableinfo', params=params).json()

# Use response.post() - note the change in the name of the parameter about the table's name
# I'm also adding here a language parameter - most tables are available in both Danish and English
params = {'table': 'metrox1', 'format': 'JSON', 'lang':'en'}
requests.post('https://api.statbank.dk/v1' + '/tableinfo', json=params).json()


# Initialize the class with the target table
metro = DstApi('METROX1')

# Get the table summary
metro.tablesummary(language='en')
metro.variable_levels('SÆSON', language='en')

dnkapk = DstApi('dnkapk')
display(dnkapk.tablesummary(language='en'))
display(dnkapk.variable_levels('INSTRUMENT', language='en'))

params = {
    'table': 'metrox1',
    'format': 'BULK',
    'variables': [
        {'code': 'SÆSON', 'values': ['10']},
        {'code': 'Tid', 'values': ['*']}
    ]
}

r = requests.post('https://api.statbank.dk/v1' + '/data', json=params)

df = pd.read_table(StringIO(r.text), sep=';')

