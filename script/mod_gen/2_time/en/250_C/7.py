def solve():
    N, Q = map(int, input().split())
    a = [i for i in range(1, N + 1)]
    for _ in range(Q):
        x = int(input())
        idx = a.index(x)
        if idx == N - 1:
            a[idx], a[0] = a[0], a[idx]
        else:
            a[idx], a[idx + 1] = a[idx + 1], a[idx]
    print(*a)

if __name__ == '__main__':
    solve()