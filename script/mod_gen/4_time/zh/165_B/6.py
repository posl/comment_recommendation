def get_year(x):
    y = 100
    year = 0
    while y < x:
        y = int(y * 1.01)
        year += 1
    return year

if __name__ == '__main__':
    get_year()