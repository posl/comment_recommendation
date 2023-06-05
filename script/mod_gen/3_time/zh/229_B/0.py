def carry(a, b):
    if a == 0 and b == 0:
        return 0
    elif a % 10 + b % 10 >= 10:
        return 1 + carry(a // 10, b // 10)
    else:
        return carry(a // 10, b // 10)
a, b = map(int, input().split())

if __name__ == '__main__':
    carry()