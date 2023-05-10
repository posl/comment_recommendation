def calc_year(x):
    year = 0
    balance = 100
    while balance < x:
        balance = balance + int(balance * 0.01)
        year += 1
    return year

if __name__ == '__main__':
    calc_year()