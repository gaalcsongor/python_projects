import requests
import tkinter as tk
from tkinter import messagebox


class GUI:
    def __init__(self):
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        btc_data = r.json() 
        self.rate_usd = btc_data["bpi"]["USD"]["rate"]
        self.rate_usd = float(self.rate_usd.replace(",", ""))
        self.rate_eur = btc_data["bpi"]["EUR"]["rate"]
        self.rate_eur = float(self.rate_eur.replace(",", ""))
        
        huf_data = requests.get("https://api.fxratesapi.com/latest")
        huf_data = huf_data.json()
        self.rate_usd_huf = huf_data["rates"]["HUF"]
        
        self.window = tk.Tk()
        self.window.title("BTC calculator")
        self.window.geometry("600x400")
        
        self.header = tk.Label(self.window, text="Calculate the price of BTC in real time", font=("Arial", 20))
        self.header.pack(padx=20, pady=20)
        
        self.line_01 = tk.Label(self.window, text="how many BTC do you want to buy?", font=("Arial", 12))
        self.line_01.pack(padx=20, pady=(20, 10))
        
        self.text_box = tk.Text(self.window, height=1, width=10, font=("Arial", 12))
        self.text_box.pack(padx=20, pady=(0, 20))
        
        self.line_02 = tk.Label(self.window, text="select the currency", font=("Arial", 12))
        self.line_02.pack(padx=20, pady=(20, 10))
        
        self.currency = tk.StringVar(self.window)
        self.currency.set("USD")
        self.dropdown = tk.OptionMenu(self.window, self.currency, "USD", "EUR", "HUF")
        self.dropdown.pack(padx=20, pady=(0, 20))
        
        self.calc_button = tk.Button(self.window, text="calculate", font=("Arial", 12), command=self.calculate)
        self.calc_button.pack(padx=20, pady=20)
    
        self.window.mainloop()
        
        
    def calculate(self):
        ammount = self.text_box.get("1.0", tk.END)
        try:
            ammount = float(ammount.replace(",", "."))
            ammount = round(ammount, 2)
        except ValueError:
            messagebox.showerror(title="error", message="you need to input a number in the text box")
        
        if self.currency.get() == "USD":
            try:
                price = round((ammount * self.rate_usd), 2)
            except TypeError:
                pass
            try:
                messagebox.showinfo(title=None, message=f"{ammount} BTC will cost {price:,.2f} USD")
            except UnboundLocalError:
                pass
        elif self.currency.get() == "EUR":
            try:
                price = round((ammount * self.rate_eur), 2)
            except TypeError:
                pass
            try:
                messagebox.showinfo(title=None, message=f"{ammount} BTC will cost {price:,.2f} EUR")
            except UnboundLocalError:
                pass
        else:
            try:
                price = (ammount * self.rate_usd) * self.rate_usd_huf
                price = round(price, 2)
            except TypeError:
                pass
            try:
                messagebox.showinfo(title=None, message=f"{ammount} BTC will cost {price:,.2f} HUF")
            except UnboundLocalError:
                pass


if __name__ == "__main__":
    calculator = GUI()