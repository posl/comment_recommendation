def solve():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a = a[::-1]
    b = b[::-1]
    ans = [-1] * (n + 1)
    for i in range(m):
        if ans[a[i]] == -1 and ans[b[i]] == -1:
            ans[a[i]] = b[i]
            ans[b[i]] = a[i]
        elif ans[a[i]] == -1:
            ans[a[i]] = b[i]
        elif ans[b[i]] == -1:
            ans[b[i]] = a[i]
        else:
            if ans[a[i]] != b[i] or ans[b[i]] != a[i]:
                print(-1)
                exit()
    for i in range(1, n + 1):
        if ans[i] == -1:
            ans[i] = i
    print(*ans[1:])

if __name__ == '__main__':
    solve()