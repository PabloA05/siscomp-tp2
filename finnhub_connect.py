import ctypes
import json
import time

import requests
import websocket

dolar_url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
euro_url = 'https://api.exchangerate-api.com/v4/latest/EUR'
ws_url = "wss://ws.finnhub.io?token=cgjlh8pr01qt0jk14jn0cgjlh8pr01qt0jk14jng"

separador = '-' * 50

# Cargando la biblioteca compartida
libconversor = ctypes.CDLL('./libconversor.so')

# Declarando la función conversor de C
libconversor.conversor.restype = ctypes.c_float
libconversor.conversor.argtypes = (ctypes.c_float, ctypes.c_float,)

# variables globales default para almacenar las cotizaciones de USDTEUR y USDTARS
USDEUR = 0.91
USDARS = 400.0


def get_fiat_price(api_url, target_currency):
    global USDARS, USDEUR
    response = requests.get(api_url)

    # Si la solicitud fue exitosa (código de estado HTTP 200),
    # extraemos el valor de la cotización del response
    if response.status_code == 200:
        data = response.json()
        # Obtenemos la tasa de conversión deseada e imprimimos el resultado
        if target_currency == "ARS":
            USDARS = [item['casa']['venta']
                      for item in data if item['casa']['nombre'] == 'Dolar Blue'][0][0:3]
            print(f'Último precio de USD/ARS: {USDARS}')
        else:
            USDEUR = round(1/data['rates']["USD"], 2)
            print(f'Último precio de USD/EUR: {USDEUR}')

    else:
        print(
            f'Error al obtener la cotización de USD/{target_currency}. '
            f'Utilizamos un valor referencia de {USDARS if target_currency == "ARS" else USDEUR}'
        )


def send_subscription(ws, symbol):
    subscription_message = {"type": "subscribe", "symbol": symbol}
    ws.send(json.dumps(subscription_message))


def on_open(ws):
    print("Web Socket Opened")
    send_subscription(ws, "BINANCE:BTCUSDT")
    send_subscription(ws, "BINANCE:ETHUSDT")

def on_close(ws):
    print("Web Socket closed connection")
    # Reconnect after a delay
    time.sleep(5)
    main()


def on_message(ws, message):
    print(separador)
    print("Empezando las conversiones de ETH o BTC a USD/ARS/EUR")
    data = json.loads(message)
    if data["type"] == "trade":
        crypto_price = data["data"][0]["p"]
        crypto_currency = "BTC" if data["data"][0]["s"] == "BINANCE:BTCUSDT" else "ETH"

        # convertir a pesos argentinos usando la función "conversor"
        ars_price = round(libconversor.conversor(float(crypto_price), float(USDARS)), 2)
        eur_price = round(libconversor.conversor(float(crypto_price), float(USDEUR)), 2)
        print(f"{crypto_currency}: USD: {crypto_price}, ARS: {ars_price}, EUR: {eur_price}")
    print("\n\nConversiones terminadas.")
    print(separador)
    time.sleep(5)


def main():
    get_fiat_price(dolar_url, "ARS")
    get_fiat_price(euro_url, "EUR")

    # Obtenemos las cotizaciones USDTEUR y USDTARS
    ws = websocket.WebSocketApp(
        ws_url, on_open=on_open, on_close=on_close, on_message=on_message
    )
    ws.run_forever()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("^C\nExiting the application.")
    except EOFError:
        print("^D\nExiting the application.")
    except Exception as e:
        print(f"Error: {e}")
        # Reconnect after a delay
        time.sleep(5)
        main()
