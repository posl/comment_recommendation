def solve():
    N = int(input())
    H = [int(i) for i in input().split()]
    cnt = 0
    ans = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)
solve()
