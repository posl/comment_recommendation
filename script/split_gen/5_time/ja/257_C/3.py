def solve():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if S[i] == '1':
            cnt += 1
    if cnt == 0 or cnt == N:
        print(N)
        return
    #累積和を作る
    cumsum = [0] * (N + 1)
    for i in range(N):
        cumsum[i + 1] = cumsum[i] + W[i]
    ans = 0
    for i in range(1, N):
        if S[i] == '1':
            continue
        #i番目の人を大人とする
        left = cumsum[i] / i
        #i番目の人を子供とする
        right = (cumsum[N] - cumsum[i]) / (N - i)
        if left < right:
            ans = max(ans, i)
    print(ans + cnt)
solve()
