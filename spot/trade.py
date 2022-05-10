import dotenv
import os
import requests

import signature.hashing

dotenv.load_dotenv()
base = os.getenv("BASE_URL")


def get_timestamp():
    url = base + "/get-timestamp"
    try:
        return requests.get(url).json()
    except Exception as error:
        print(error)
        return


def get_open_buy_sell_order(symbol, t, receive_window):
    url = base + "/get-open-buy-sell-order"
    timestamp = get_timestamp()["timestamp"]
    headers = {"api-key": _get_api_key()}
    params = {"symbol": symbol,
              "type": t,
              "timestamp": timestamp,
              "receive_window": receive_window,
              "signature": signature.hashing.query_string(f"{symbol}:{t}")}
    resp = requests.get(url, params=params, headers=headers)
    return resp.content


def get_user_open_order(symbol, t, receive_window):
    url = base + "/get-user-open-order"
    timestamp = get_timestamp()["timestamp"]
    headers = {"api-key": _get_api_key()}
    params = {"symbol": symbol,
              "type": t,
              "timestamp": timestamp,
              "receive_window": receive_window,
              "signature": signature.hashing.query_string(f"{symbol}:{t}")}
    resp = requests.get(url, params=params, headers=headers)
    return resp.content


def _get_api_key():
    return os.getenv("KEY")
