def main():
    n, m = map(int, input().split())
    g = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].add(b-1)
        g[b-1].add(a-1)
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if j in g[i] and k in g[i] and k in g[j]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()