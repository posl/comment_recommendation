def main():
    n, m = map(int, input().split())
    k = []
    a = []
    for _ in range(m):
        k.append(int(input()))
        a.append(list(map(int, input().split())))
    count = [0] * (n + 1)
    for i in range(m):
        for j in range(k[i]):
            count[a[i][j]] += 1
    for i in range(1, n + 1):
        if count[i] % 2 != 0:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()