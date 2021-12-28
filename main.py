from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import *
import json
      
def get_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
        }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '086585a3-381b-4a4b-90a2-eb2bdb9e4faa',
        }
        
    session = Session()
    session.headers.update(headers)
        
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    
    

def creat_txt_file(data):
    now = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    file = open('data/'+ now +'.txt' , 'w')
    file.write(str(data))
    file.close()

creat_txt_file(get_data())
print("The information file was saved.")



''' for i in range(501):
        file.write(""+str(i)+"-------"+"--time = "+now+"----------\n")
        file.write('Name                       :'+str(data['data'][i]['name']))
        file.write('\nSymbol                    :'+str(data['data'][i]['symbol']))
        file.write('\nprice (USD)               :'+str(data['data'][i]['quote']['USD']['price']))
        file.write('\nvolime_24h (USD)          :'+str(data['data'][i]['quote']['USD']['volume_24h']))
        file.write('\nvolime_change_24h (USD)   :'+str(data['data'][i]['quote']['USD']['volume_change_24h']))
        file.write('\npercent_change_1h (USD)   :'+str(data['data'][i]['quote']['USD']['percent_change_1h']))
        file.write('\npercent_change_24h (USD)  :'+str(data['data'][i]['quote']['USD']['percent_change_24h']))
        file.write('\npercent_change_7d (USD)   :'+str(data['data'][i]['quote']['USD']['percent_change_7d']))
        file.write('\npercent_change_30d (USD)  :'+str(data['data'][i]['quote']['USD']['percent_change_30d']))
        file.write('\npercent_change_60d (USD)  :'+str(data['data'][i]['quote']['USD']['percent_change_60d']))
        file.write('\npercent_change_90d (USD)  :'+str(data['data'][i]['quote']['USD']['percent_change_90d']))
        file.write('\nmarket_cap (USD)          :'+str(data['data'][i]['quote']['USD']['market_cap']))
        file.write('\nmarket_cap_dominance (USD):'+str(data['data'][i]['quote']['USD']['market_cap_dominance']))
        file.write('\nfully_diluted_market_cap (USD):'+str(data['data'][i]['quote']['USD']['fully_diluted_market_cap']))
        file.write('\nlast_updated (USD) :'+str(data['data'][i]['quote']['USD']['last_updated']))
        file.write('\n') '''