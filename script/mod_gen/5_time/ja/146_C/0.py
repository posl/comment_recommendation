def calc_price(a, b, n):
    return a * n + b * len(str(n))
a, b, x = map(int, input().split())

if __name__ == '__main__':
    calc_price()