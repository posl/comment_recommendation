def discounted_price():
    a, b = map(int, input().split())
    print((a - b) / a * 100)

if __name__ == '__main__':
    discounted_price()