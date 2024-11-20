import requests
import time

class BitCoinFetcher:
    def __init__(self):
        self.PRICES = []
    # function that uses the api by https://www.coindesk.com/ to get the current value of bitcoin in US dollars.
    # if can fetch, returns current value (float). if can't fetch, returns none.
    def fetch_bitcoin_price(self):
        try:
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
            bitcoin_value = response.json()['bpi']['USD']['rate_float']
            return bitcoin_value
        except requests.exceptions.RequestException as e:
            return None

    # function that calculates the avg of prices and prints it.
    def prices_avg(self):
        # if no prices in array, return none
        if len(self.PRICES) == 0:
            return None
        # every 10 minutes, print the average value of the last 10 minutes
        avg = sum(self.PRICES) / len(self.PRICES)
        # reset array of 10 last values and return value
        self.PRICES = []
        return avg

    # function that prints the required data (value every minute, and avg every 10 minutes)
    def print_data(self):
        # if fetched current value, print it
        bitcoin_value = self.fetch_bitcoin_price()
        if bitcoin_value is not None:
            print(f"Current bitcoin value: {bitcoin_value}")
            self.PRICES.append(bitcoin_value)
        # if 10 minutes passed, print average
        if len(self.PRICES) == 10:
            cur_avg = self.prices_avg()
            print(f"Average bitcoin value of last 10 minutes: {cur_avg}")

if __name__ == "__main__":
    bf = BitCoinFetcher()
    while True:
        try:
            # fetch every 1 minute and print current data
            bf.print_data()
            time.sleep(60) 
        except Exception as e:
            # catch exceptions to avoid sudden crashing
            print(f"An error occurred: {e}")
