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
              "signature": signature.hashing.query_string(f"{symbol}")}
    resp = requests.get(url, params=params, headers=headers)
    return resp.content


def check_user_balance(symbol, receive_window):
    url = base + "/check-user-balance"
    timestamp = get_timestamp()["timestamp"]
    headers = {"api-key": _get_api_key()}
    params = {"symbol": symbol,
              "timestamp": timestamp,
              "receive_window": receive_window,
              "signature": signature.hashing.query_string(f"{symbol}")}
    resp = requests.get(url, params=params, headers=headers)
    return resp.content


def get_market_price(symbol, receive_window):
    url = base + "/get-market-price"
    timestamp = get_timestamp()["timestamp"]
    headers = {"api-key": _get_api_key()}
    params = {"symbol": symbol,
              "timestamp": timestamp,
              "receive_window": receive_window}
    resp = requests.get(url, params=params, headers=headers)
    return resp.content


def get_market_price_all(receive_window):
    url = base + "/get-market-price"
    timestamp = get_timestamp()["timestamp"]
    headers = {"api-key": _get_api_key()}
    params = {"timestamp": timestamp,
              "receive_window": receive_window}
    resp = requests.get(url, params=params, headers=headers)
    return resp.content


# limit_or_market 1-LIMIT 2-MARKET
# sell_or_buy 1-BUY 2-SELL
def place_order(symbol, limit_or_market, price, sell_or_buy, qty, receive_window):
    url = base + "/trade-bot"
    timestamp = get_timestamp()["timestamp"]
    headers = {"api-key": _get_api_key()}
    # "Symbol:order_type:price:qty:type:timestamp:receive_window
    sig = signature.hashing.query_string(
        f"{symbol}:{limit_or_market}:{price}:{qty}:{sell_or_buy}:{timestamp}:{receive_window}")
    data = {"timestamp": timestamp,
            "receive_window": receive_window,
            "symbol": symbol,
            "order_type": limit_or_market,
            "price": price,
            "type": sell_or_buy,
            "qty": qty,
            "signature": sig}

    resp = requests.post(url, data=data, headers=headers)
    return resp.content


def cancel_user_trade(trade_id, receive_window):
    url = base + '/cancel-user-trade'
    timestamp = get_timestamp()["timestamp"]
    headers = {"api-key": _get_api_key()}
    sig = signature.hashing.query_string(f"{trade_id}")
    params = {"timestamp": timestamp,
              "receive_window": receive_window,
              "id": trade_id,
              "signature": sig}

    resp = requests.get(url, params=params, headers=headers)
    return resp.content


# 1-Limit, 2-Market, 3-Stop Limit
def cancel_user_bulk_order(order_type, receive_window):
    url = base + '/cancel-bulk-order'
    timestamp = get_timestamp()["timestamp"]
    headers = {"api-key": _get_api_key()}
    sig = signature.hashing.query_string(f"{order_type}")
    params = {"timestamp": timestamp,
              "receive_window": receive_window,
              "type": order_type,
              "signature": sig}

    resp = requests.get(url, params=params, headers=headers)
    return resp.content


def _get_api_key():
    return os.getenv("KEY")
