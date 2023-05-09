def main():
    n, m, k = map(int, input().split())
    f = [set() for _ in range(n)]
    b = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        f[a - 1].add(b - 1)
        f[b - 1].add(a - 1)
    for _ in range(k):
        c, d = map(int, input().split())
        b[c - 1].add(d - 1)
        b[d - 1].add(c - 1)
    ans = [0] * n
    for i in range(n):
        ans[i] = n - len(f[i]) - 1 - len(b[i])
    for i in range(n):
        for j in f[i]:
            if i in f[j]:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(n):
        print(ans[i], end=" ")
    print()

if __name__ == '__main__':
    main()