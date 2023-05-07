def solve():
    N, K = map(int, input().split())
    friend = []
    for _ in range(N):
        A, B = map(int, input().split())
        friend.append((A, B))
    friend.sort()
    ans = 0
    i = 0
    while K > 0:
        if i == N:
            ans += K
            break
        if friend[i][0] - ans > 1:
            if K < (friend[i][0] - ans - 1):
                ans += K
                break
            else:
                K -= (friend[i][0] - ans - 1)
                ans += (friend[i][0] - ans - 1)
        K += friend[i][1]
        ans += 1
        i += 1
    print(ans)
