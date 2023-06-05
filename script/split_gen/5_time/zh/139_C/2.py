def solve():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(1, N):
        if H[i-1] >= H[i]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)
solve()
