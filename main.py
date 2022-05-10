import signature.hashing
import spot.trade


def main():
    print(signature.hashing.query_string("BTC_USDT:0"))


print(spot.trade.get_timestamp())
print(spot.trade.get_open_buy_sell_order("BTC_USDT", 0, 2000))
print(spot.trade.get_user_open_order("BTC_USDT", 0, 2000))
