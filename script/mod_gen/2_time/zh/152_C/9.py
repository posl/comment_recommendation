def solve():
    n = int(input())
    p = list(map(int, input().split()))
    min_ = p[0]
    ans = 1
    for i in range(1, n):
        if p[i] <= min_:
            ans += 1
        min_ = min(min_, p[i])
    print(ans)

if __name__ == '__main__':
    solve()