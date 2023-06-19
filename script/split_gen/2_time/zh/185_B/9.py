def solve():
    n,m,t = map(int,input().split())
    ab = []
    for i in range(m):
        ab.append(list(map(int,input().split())))
    ans = "Yes"
    now = 0
    for i in range(m):
        if i == 0:
            now += ab[i][0]
        else:
            now += ab[i][0] - ab[i-1][1]
        if now >= n:
            now = n
        now -= ab[i][1] - ab[i][0]
        if now <= 0:
            ans = "No"
            break
    if ans == "Yes":
        now += t - ab[-1][1]
        if now >= n:
            now = n
        now -= t
        if now <= 0:
            ans = "No"
    print(ans)
