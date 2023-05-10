def main():
    N = int(input())
    A = list(map(int, input().split()))
    # dp[i][j] := i番目までの整数の中からいくつか選んで、その総和を200で割った余りがjであるような選び方が存在するかどうか
    dp = [[False] * 200 for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(200):
            # i番目の整数を選ぶ場合
            dp[i+1][j] |= dp[i][j]
            # i番目の整数を選ばない場合
            dp[i+1][(j+A[i])%200] |= dp[i][j]
    if dp[N][0] == False:
        print('No')
        return
    print('Yes')
    # dp[N][0] == True となるような選び方を復元する
    ans = []
    i = N
    j = 0
    while i > 0:
        # i番目の整数を選ばなかった場合
        if dp[i-1][j]:
            i -= 1
        # i番目の整数を選んだ場合
        else:
            ans.append(i)
            j = (j - A[i-1]) % 200
            i -= 1
    print(len(ans), *ans)
    i = N
    j = 0
    while i > 0:
        if dp[i-1][j]:
            i -= 1
        else:
            ans.append(i)
            j = (j - A[i-1]) % 200
            i -= 1
    print(len(ans), *ans)
