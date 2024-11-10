# btc price calculator created by cs in 2024
# this program calculates the price of btc in USD and EUR depending
# on the user prompt // it uses the coinbase API to get the data

import sys
import requests

def main():
    print("\n*****************************************")
    print("*        BTC price calculator           *")
    print("*****************************************\n")
    
    price_usd, price_eur = get_data()
    currency, ammount = get_user_input()
    
    if currency == "usd":
        final_price = price_usd * ammount
        print(f"\nit will cost you: {final_price:,.4f} USD")
    elif currency == "eur":
        final_price = price_eur * ammount
        print(f"\nit will cost you: {final_price:,.4f} EUR")

    
def get_data():
    """make the https request and convert to json format"""
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r = response.json()

    usd = r["bpi"]["USD"]["rate"]
    usd = float(usd.replace(",", ""))
    eur = r["bpi"]["EUR"]["rate"]
    eur = float(eur.replace(",", ""))
    
    return usd, eur


def get_user_input():
    """prompts the user for the currency and ammount"""
    while True:
        user_currency = input("do you want to buy BTC in USD or EUR? ")
        if user_currency.lower() == "q":
            sys.exit()
        elif user_currency.lower() == "usd":
            while True:
                try: 
                    user_ammount = (input("how much do you want to buy? "))
                    if user_ammount.lower() == "q":
                        sys.exit()
                    user_ammount = float(user_ammount) 
                except ValueError:
                    print("you need to give a number")
                    continue
                return user_currency, user_ammount
        elif user_currency.lower() == "eur":
            while True:
                try: 
                    user_ammount = (input("how much do you want to buy? "))
                    if user_ammount.lower() == "q":
                        sys.exit()
                    user_ammount = float(user_ammount)
                except ValueError:
                    print("you need to give a number")
                    continue
                return user_currency, user_ammount
        else:
            print("you need to type 'usd' or 'eur'!")
            continue


if __name__ == "__main__":
    main()