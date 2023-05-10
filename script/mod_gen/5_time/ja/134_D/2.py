def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in reversed(range(1, n + 1)):
        s = sum(b[i - 1::i]) % 2
        if s != a[i - 1]:
            b[i - 1] = 1
    m = sum(b)
    if m == 0:
        print(0)
    else:
        print(m)
        print(*[i + 1 for i, j in enumerate(b) if j == 1])

if __name__ == '__main__':
    main()