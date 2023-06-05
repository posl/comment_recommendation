def coin_pay(coin_list, pay):
    coin_list.sort(key=lambda x: x[0], reverse=True)
    pay_list = []
    for coin in coin_list:
        for i in range(coin[1]):
            pay_list.append(coin[0])
    pay_list.sort(reverse=True)
    pay_sum = 0
    for coin in pay_list:
        pay_sum += coin
        if pay_sum == pay:
            return True
    return False
