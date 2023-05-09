def get_price():
    a, b = map(int, input().split())
    for i in range(1, 100):
        if (i * 0.08) // 1 == a and (i * 0.1) // 1 == b:
            return i
    return -1
print(get_price())

if __name__ == '__main__':
    get_price()