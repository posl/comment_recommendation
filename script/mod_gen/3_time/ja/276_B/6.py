def solve():
    N, M = map(int, input().split())
    d = [0] * N
    a = [[] for _ in range(N)]
    for i in range(M):
        x, y = map(int, input().split())
        d[x - 1] += 1
        d[y - 1] += 1
        a[x - 1].append(y - 1)
        a[y - 1].append(x - 1)
    for i in range(N):
        a[i].sort()
    for i in range(N):
        print(d[i], *map(lambda x: x + 1, a[i]))

if __name__ == '__main__':
    solve()