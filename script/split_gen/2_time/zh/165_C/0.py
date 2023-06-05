def problem165_b(x):
    balance = 100
    year = 0
    while balance < x:
        balance = int(balance * 1.01)
        year += 1
    return year
