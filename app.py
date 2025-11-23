import os
import requests

cle = input("Votre clé API pour ALPHAVANTAGE (une clé est disponible dans la question 2 du Labo5) : ")
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", cle)
BASE_URL = "https://www.alphavantage.co/query"

SYMBOLS = ["MSFT", "AAPL", "GOOGL", "AMZN", "META"]

def get_global_quote(symbol: str) -> dict | None:
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY,
    }
    resp = requests.get(BASE_URL, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    quote = data.get("Global Quote") or data.get("Global_Quote")
    if not quote:
        return None
    return quote

def main():
    print("Cours des titres (Alpha Vantage) :")
    for symbol in SYMBOLS:
        try:
            quote = get_global_quote(symbol)
        except Exception as e:
            print(f"- {symbol} : erreur de requête ({e})")
            continue

        if not quote:
            print(f"- {symbol} : aucune donnée renvoyée")
            continue

        price = quote.get("05. price") or quote.get("05. Price")
        currency = "USD"
        print(f"- {symbol} : {price} {currency}")

if __name__ == "__main__":
    main()
