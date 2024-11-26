import pandas as pd
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from time import sleep
import config

def api_runner():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 

    parameters = {
    'start':'1',
    'limit':'15',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': config.COINMARKET_API,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        #   print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.float_format', lambda x: '%.5f' % x)

    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')

    if not os.path.exists(r"C:/Users/pras3/source/Workspace/data-analyst-projects/Python-Projects/automate-api-extraction/api_data_collector.csv"):
        df.to_csv(r"C:/Users/pras3/source/Workspace/data-analyst-projects/Python-Projects/automate-api-extraction/api_data_collector.csv", header = 'column_names')
    else:
        df.to_csv(r"C:/Users/pras3/source/Workspace/data-analyst-projects/Python-Projects/automate-api-extraction/api_data_collector.csv", mode = 'a', header = False)

for i in range(10):
    api_runner()
    print('API Runner completed')
    sleep(60)
    pass
exit()
