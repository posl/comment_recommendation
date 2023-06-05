def get_min_coin_num(P):
    coin_num = 0
    for i in range(10,0,-1):
        coin_num += P // factorial(i)
        P %= factorial(i)
    return coin_num
