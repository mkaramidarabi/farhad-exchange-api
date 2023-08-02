import string
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
    url = base + "/v1/get-market-price"
    timestamp = get_timestamp()["timestamp"]
    headers = {"api-key": _get_api_key()}
    params = {"symbol": symbol,
              "timestamp": timestamp,
              "receive_window": receive_window}
    resp = requests.get(url, params=params, headers=headers)
    return resp.content

def generate_address(symbol, receive_window):
    url = base + "/v1/generate-deposit-wallet-address"
    timestamp = get_timestamp()["timestamp"]
    sig_str = "َUSDT"
    sig = signature.hashing.query_string(sig_str)
    headers = {"api-key": _get_api_key()}
    params = {"currency": "َUSDT",
              "timestamp": timestamp,
              "signature": sig,
              "receive_window": receive_window}

    resp = requests.post(url, params=params, headers=headers)
    return resp.content

#get-deposit-transaction-list

def get_deposit_transaction_list(symbol, receive_window):
    url = base + "/v1/get-deposit-transaction-list"
    timestamp = get_timestamp()["timestamp"]
    sig_str = "DOGE"
    # sig = signature.hashing.query_string(sig_str)
    headers = {"api-key": _get_api_key()}
    params = {"page": "1",
              "timestamp": timestamp,
              # "signature": sig,
              "receive_window": receive_window}

    resp = requests.post(url, params=params, headers=headers)
    return resp.content

#/v1/get-withdraw-transaction-list
def get_withdraw_transaction_list(symbol, receive_window):
    url = base + "/v1/get-withdraw-transaction-list"
    timestamp = get_timestamp()["timestamp"]
    sig_str = "DOGE"
    # sig = signature.hashing.query_string(sig_str)
    headers = {"api-key": _get_api_key()}
    params = {"page": "1",
              "timestamp": timestamp,
              # "signature": sig,
              "receive_window": receive_window}

    resp = requests.post(url, params=params, headers=headers)
    return resp.content

def get_reserve(symbol, receive_window):
    url = base + "/v1/rapid/get-reserve"
    timestamp = get_timestamp()["timestamp"]
    sig_str = "SELL:1000:USDT/IRR:2000"
    sig = signature.hashing.query_string(sig_str)
    headers = {"api-key": _get_api_key()}
    params = {"type": "SELL",
              "amountFrom": "1000",
              "timestamp": timestamp,
              "pair": "USDT/IRR",
              "signature": sig,
              "receive_window": receive_window}

    resp = requests.post(url, params=params, headers=headers)
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
	print("limit Orders")
	url = base + "/v1/trade-bot"
	timestamp = get_timestamp()["timestamp"]
	headers = {"api-key": _get_api_key()}
	# "Symbol:order_type:price:qty:type:timestamp:receive_window
	sig_str = f"{symbol}:{limit_or_market}:{price}:{qty}:{sell_or_buy}:{timestamp}:{receive_window}"
	sig = signature.hashing.query_string(sig_str)
	print(sig_str)
	print(sig)
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

def withdraw(currency_code, fromAddress, toAddress, network, amount, fromMemo, memo):
	url = base + "/v1/create-withdraw-transaction"
	timestamp = get_timestamp()["timestamp"]
	headers = {"api-key": _get_api_key()}
	# "Symbol:order_type:price:qty:type:timestamp:receive_window
	sig_str = f"{fromAddress}:{toAddress}:{currency_code}:{network}:{amount}:20000"
	print(sig_str)
	sig = signature.hashing.query_string(sig_str)
	print(sig_str)
	print(sig)
	print(timestamp)
	data = {
          timestamp: timestamp,
         	"receive_window": "20000",
					currency_code: currency_code,
					fromAddress: fromAddress,
					"fromMemo": "null",
					toAddress: toAddress,
					"memo": "null",
					network: network,
					amount: amount,
          signature: sig}

	print(url)
	# resp = requests.post(url, data=data, headers=headers)
	# return resp.content


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

def place_order_by_amount(symbol, amount, sell_or_buy, receive_window):
	print("Order By Amount")
	url = base + "/trade-bot"
	timestamp = get_timestamp()["timestamp"]
	headers = {"api-key": _get_api_key()}
	# "Symbol:order_type:order_by:amount:type:timestamp:receive_window"
	sig_str = f"{symbol}:2:2:{amount}:{sell_or_buy}:{timestamp}:{receive_window}"
	sig = signature.hashing.query_string(sig_str)
	print(sig_str)
	print(sig)
	data = {"timestamp": timestamp,
					"receive_window": receive_window,
					"symbol": symbol,
					"order_type": 2,
					"order_by": 2,
					"amount": amount,
					"type": sell_or_buy,
					"signature": sig}

	resp = requests.post(url, data=data, headers=headers)
	return resp.content


def place_order_by_qty(symbol, qty, sell_or_buy, receive_window):
	print("Order By QTY")
	url = base + "/trade-bot"
	timestamp = get_timestamp()["timestamp"]
	headers = {"api-key": _get_api_key()}
	# "Symbol:order_type:order_by:qty:type:timestamp:receive_window"
	sig_str = f"{symbol}:2:1:{qty}:{sell_or_buy}:{timestamp}:{receive_window}"
	sig = signature.hashing.query_string(sig_str)
	print(sig_str)
	print(sig)
	data = {"timestamp": timestamp,
				"receive_window": receive_window,
				"symbol": symbol,
				"order_type": 2,
				"order_by": 1,
				"type": sell_or_buy,
				"qty": qty,
				"signature": sig}

	resp = requests.post(url, data=data, headers=headers)
	return resp.content


def _get_api_key():
    return os.getenv("KEY")
