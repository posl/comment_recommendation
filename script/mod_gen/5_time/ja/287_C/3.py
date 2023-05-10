def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    for i in range(n):
        if len(g[i]) == 2:
            continue
        else:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()