def calc(n, k):
    if k % 2 == 0:
        a = n // k
        b = n // (k // 2) - a
        c = n // (k // 2) - a
        return a ** 3 + b ** 3 + c ** 3
    else:
        a = n // k
        b = n // (k // 2) - a
        c = n // (k // 2) - a
        d = n // (k // 2 + 1) - a
        return a ** 3 + b ** 3 + c ** 3 + d ** 3
n, k = map(int, input().split())
print(calc(n, k))

if __name__ == '__main__':
    calc()