def get_max_joy(money):
    joy = 0
    coins = [500,100,50,10,5,1]
    for coin in coins:
        joy += money // coin
        money = money % coin
    return joy
