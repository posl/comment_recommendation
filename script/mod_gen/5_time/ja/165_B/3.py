def calc_year(x):
    year = 0
    while x > 100:
        x = x * 101 // 100
        year += 1
    return year

if __name__ == '__main__':
    calc_year()