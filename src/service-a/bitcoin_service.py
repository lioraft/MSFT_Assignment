import requests
import time

PRICES = []

# function that uses the api by https://www.coindesk.com/ to get the current value of bitcoin in US dollars.
# if can fetch, returns current value (float). if can't fetch, returns none.
def fetch_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
        bitcoin_value = response.json()['bpi']['USD']['rate_float']
        return bitcoin_value
    except requests.exceptions.RequestException as e:
        print(f"Error fetching bitcoin price: {e}")
        return None

# function that calculates the avg of last 10 minutes and prints it.
def ten_min_avg():
    global PRICES
    # every 10 minutes, print the average value of the last 10 minutes
    if len(PRICES) == 10:
        avg = sum(PRICES) / 10
        # reset array of 10 last values
        PRICES = []
        print(f"Average bitcoin value of last 10 minutes: {avg}")

# function that prints the required data (value every minute, and avg every 10 minutes)
def print_data():
    bitcoin_value = fetch_bitcoin_price()
    if bitcoin_value is not None:
        print(f"Current bitcoin value: {bitcoin_value}")
        PRICES.append(bitcoin_value)
    else:
        print("Bitcoin value not fetched due to internal error")


while True:
    try:
        print_data() # print current data
        time.sleep(60)  # fetch every 1 minute
    except Exception as e:
        print(f"An error occurred: {e}") # catch exceptions to avoid sudden crashing
