def solve():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = n*m - s
    if ans > k:
        print(-1)
    elif ans < 0:
        print(0)
    else:
        print(ans)

if __name__ == '__main__':
    solve()