import requests
import json
from datetime import datetime
from src.config import(
        EXCHANGE_RATE_API_KEY,
        DEFAULT_CURRENCIES,
        REQUEST_TIMEOUT,
   
)


def fetch_data_from_api():

    all_currencies = []
   

    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/latest/USD"

   
    
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)

        if response.status_code == 200:
            data = response.json()
            
            selected_cuurencies = {
                 currency: data["conversion_rates"].get(currency)
                  for currency in DEFAULT_CURRENCIES }
            
            for currency, rate in selected_cuurencies.items():
             currencies_record = {
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                "base_code": data["base_code"],
                "target_currency":currency,
                "exchange_rate": rate
              
                }
            
             all_currencies.append(currencies_record)
        


        else:
            print("API request failed:", response.status_code)

    except requests.exceptions.RequestException as error:
        print("Network error:", error)

    return all_currencies

if __name__ == "__main__":
    result = fetch_data_from_api()
    print(result)



 


