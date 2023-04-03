import websocket
import json

def on_open(ws):
    print("opened")
    subscribe_message = {
        "type": "subscribe",
        "symbol": "BINANCE:BTCUSDT"
    }
    subscribe_message_json = json.dumps(subscribe_message)
    ws.send(subscribe_message_json)

    subscribe_message = {
        "type": "subscribe",
        "symbol": "BINANCE:ETHUSDT"
    }
    subscribe_message_json = json.dumps(subscribe_message)
    ws.send(subscribe_message_json)

def on_close(ws):
    print("closed connection")

def on_message(ws, message):
    data = json.loads(message)
    if data["type"] == "trade":
        if data["data"][0]["s"] == "BINANCE:BTCUSDT":
            btc_price = data["data"][0]["p"]
            print(f"BTC: {btc_price}")
        elif data["data"][0]["s"] == "BINANCE:ETHUSDT":
            eth_price = data["data"][0]["p"]
            print(f"ETH: {eth_price}")

socket = "wss://ws.finnhub.io?token=cgjlh8pr01qt0jk14jn0cgjlh8pr01qt0jk14jng"
ws = websocket.WebSocketApp(socket, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()