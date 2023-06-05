def main():
    l = int(input())
    n = 2
    m = 2
    while n < l:
        n *= 2
        m += 1
    print(n, m)
    for i in range(1, m):
        print(i, i + 1, 0)
        print(i, i + 1, 2 ** (i - 1))
    l -= n // 2
    for i in range(m - 1, 0, -1):
        if l >= 2 ** (i - 1):
            print(i, m, l)
            l -= 2 ** (i - 1)
