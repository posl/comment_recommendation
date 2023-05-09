def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #累積和を求める
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    #累積和の差分を求める
    D = [0] * (N + 1)
    for i in range(N):
        D[i + 1] = S[i + 1] - K
    #累積和の差分をソート
    D.sort()
    #累積和の差分の同じものを探す
    ans = 0
    i = 0
    while i < N:
        cnt = 1
        while i < N and D[i] == D[i + 1]:
            cnt += 1
            i += 1
        ans += cnt * (cnt - 1) // 2
        i += 1
    print(ans)
