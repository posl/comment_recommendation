def main():
    n, m = map(int, input().split())
    d = [0] * n
    a = [[] for _ in range(n)]
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        d[ai] += 1
        d[bi] += 1
        a[ai].append(bi)
        a[bi].append(ai)
    for i in range(n):
        print(d[i], end=' ')
        for j in range(d[i]):
            print(a[i][j] + 1, end=' ')
        print()

if __name__ == '__main__':
    main()