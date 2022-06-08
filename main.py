import signature.hashing
import spot.trade


def main():
    print(signature.hashing.query_string("BTC_USDT:0"))


print(spot.trade.get_timestamp())
print(spot.trade.get_open_buy_sell_order("BTC_USDT", 0, 2000))
print(spot.trade.get_user_open_order("TRON_IRR", 0, 2000))
print(spot.trade.check_user_balance("TRON", 2000))
print(spot.trade.get_market_price("DOGE_USDT", 2000))
print(spot.trade.get_market_price_all(2000))

# place buy or sell order
# print(spot.trade.place_order("TRON_IRR", 1, 0.001, 1, 200001000, 2000))
# cancel an order via order id
# print(spot.trade.cancel_user_trade(127413727, 2000))
# Other user's order
# print(spot.trade.cancel_user_trade(127413727, 2000))
# 1-Limit, 2-Market, 3-Stop Limit
print(spot.trade.cancel_user_bulk_order(1, 2000))
