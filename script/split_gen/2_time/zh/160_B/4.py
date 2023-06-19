def get_max_happiness_point(money):
    happiness = 0
    happiness += money // 500 * 1000
    happiness += (money % 500) // 5 * 5
    return happiness
