import tkinter as tk
import requests
import json
import os

CACHE_FILE = "kursy.json"

def get_rates():
    try:
        url = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
        response = requests.get(url, timeout=5)
        data = response.json()
        rates = {item["code"]: item["mid"] for item in data[0]["rates"]}
        rates["PLN"] = 1.0 
        with open(CACHE_FILE, "w") as f:
            json.dump(rates, f)
        return rates
    except:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as f:
                return json.load(f)
        else:
            return {"PLN": 1.0}

# Funkcja przeliczająca waluty
def convert():
    try:
        amount = float(entry_amount.get())
        from_curr = var_from.get()
        to_curr = var_to.get()
        rate = amount * rates[from_curr] / rates[to_curr]
        label_result.config(text=f"{amount:.2f} {from_curr} = {rate:.2f} {to_curr}")
    except:
        label_result.config(text="Błąd danych")

# kursy
rates = get_rates()
currency_list = sorted(rates.keys())

# okno
root = tk.Tk()
root.title("Kalkulator Walut")

# kwota
tk.Label(root, text="Kwota:").grid(row=0, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1)

# z jakiej
tk.Label(root, text="Z:").grid(row=1, column=0)
var_from = tk.StringVar(value="PLN")
tk.OptionMenu(root, var_from, *currency_list).grid(row=1, column=1)

# na jaką
tk.Label(root, text="Na:").grid(row=2, column=0)
var_to = tk.StringVar(value="USD")
tk.OptionMenu(root, var_to, *currency_list).grid(row=2, column=1)

# przycisk
tk.Button(root, text="Przelicz", command=convert).grid(row=3, column=0, columnspan=2, pady=5)

# wynik
label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2, pady=5)


root.mainloop()
