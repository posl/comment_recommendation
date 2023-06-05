def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = [0] * n
    d[0] = 1
    i = 0
    while True:
        i = a[i] - 1
        d[i] += 1
        if d[i] == 2:
            break
    for i in range(n):
        if d[i] == 2:
            break
    k %= d[i] - 1
    for _ in range(k):
        i = a[i] - 1
    print(i + 1)

if __name__ == '__main__':
    main()