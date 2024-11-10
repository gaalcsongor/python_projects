# calculate the price of buying BTC real time in USD, EUR and HUF
import requests

def main():
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = r.json()

    rate_usd = data["bpi"]["USD"]["rate"]
    rate_usd = float(rate_usd.replace(",", ""))
    rate_eur = data["bpi"]["EUR"]["rate"]
    rate_eur = float(rate_eur.replace(",", ""))
    
    ammount = get_user_ammount()
    currency = choose_currency()
    
    if currency == 0:
        price = round(calculate_price(ammount, rate_usd), 0)
        print(f"{ammount} BTC will cost {price:,.0f} USD.")
    elif currency == 1:
        price = round(calculate_price(ammount, rate_eur), 0)
        print(f"{ammount} BTC will cost {price:,.0f} EUR.")
    else:
        huf = requests.get("https://api.fxratesapi.com/latest")
        huf_data = huf.json()
        rate_usd_huf = huf_data["rates"]["HUF"]
        price = round((calculate_price(ammount, rate_usd) * rate_usd_huf), 0)
        print(f"{ammount} BTC will cost {price:,.0f} HUF.")

        
def get_user_ammount():
    while True:
        try:
            user_ammount = float(input("how many BTC do you want to buy? "))
        except ValueError:
            print("you have to add a number!")
            continue
        return round(user_ammount, 4)
    
    
def choose_currency():
    while True:
        currency = input("do you want to buy in USD, EUR, or HUF? ").lower()
        if currency == "usd":
            return 0
        elif currency == "eur":
            return 1
        elif currency == "huf":
            return 2
        else:
            print("not a valid choice!")
            continue
    
    
def calculate_price(ammount, rate):
    price = ammount * rate
    return round(price, 2)
    

if __name__ == "__main__":
    main()
    
