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