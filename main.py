import signature.hashing
import spot.trade


def main():
    print(signature.hashing.query_string("BTC_USDT:0"))

print(signature.hashing.query_string("BTC_USDT:0"))


# print(spot.trade.get_timestamp())
# print(spot.trade.get_open_buy_sell_order("USDT_TRY", 0, 2000))
print(spot.trade.generate_address("USDT", 2000))
# print(spot.trade.get_deposit_transaction_list("USDT_TRY", 2000))
# print(spot.trade.get_withdraw_transaction_list("USDT_TRY", 2000))
# print(spot.trade.get_reserve("USDT_TRY", 2000))
print(spot.trade.withdraw("USDT", "TAP8tFmKqsU2XDaYaJFh9SAbuWTapbHob7", "TAP8tFmKqsU2XDaYaJFh9SAbuWTapbHob7", "TRC20", 2,None, None))
# print(spot.trade.get_user_open_order("TRON_IRR", 0, 2000))
# print(spot.trade.check_user_balance("TRON", 2000))
# print(spot.trade.get_market_price("USDT_TRY", 2000))
# print(spot.trade.get_market_price_all(2000))

# place buy or sell order
# print(spot.trade.place_order("USDT_IRR", 1, 477000, 1, 50, 2000))
# print(spot.trade.place_order("TRON_IRR", 1, 20000, 1, 50, 2000))
# print(spot.trade.place_order_by_amount('USDT_IRR', 10000000, 1, 2000))
# print(spot.trade.place_order_by_qty('USDT_IRR', 5, 1, 2000))
# cancel an order via order id
# print(spot.trade.cancel_user_trade(127413727, 2000))
# Other user's order
# print(spot.trade.cancel_user_trade(136675272, 2000))
# 1-Limit, 2-Market, 3-Stop Limit
# print(spot.trade.cancel_user_bulk_order(1, 2000))
# print(spot.trade.cancel_user_bulk_order(1, 2000))


# print(spot.trade.get_open_buy_sell_order('PMV_IRR', 1, 2000))
# print('HIII')
# print(spot.trade.get_open_buy_sell_order('PMV_IRR', 2, 2000))