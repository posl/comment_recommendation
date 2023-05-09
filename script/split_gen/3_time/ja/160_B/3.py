def calculate_happiness(x):
    happiness = 0
    happiness += (x // 500) * 1000
    x = x % 500
    happiness += (x // 5) * 5
    return happiness
