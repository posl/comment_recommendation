def solve():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    #print(a)
    #print(b)
    #dp = [[0 for i in range(w+1)] for j in range(n+1)]
    dp = [0 for i in range(w+1)]
    for i in range(n):
        for j in range(w, a[i]-1, -1):
            dp[j] = max(dp[j], dp[j-a[i]] + b[i])
    print(dp[w])
