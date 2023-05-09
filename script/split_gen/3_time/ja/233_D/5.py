def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    #累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    #print(S)
    #累積和の差分
    S_diff = [0] * (N + 1)
    for i in range(N):
        S_diff[i + 1] = S[i + 1] - K
    #print(S_diff)
    #累積和の差分の要素の出現回数
    S_diff_count = {}
    for i in range(N + 1):
        S_diff_count[S_diff[i]] = S_diff_count.get(S_diff[i], 0) + 1
    #print(S_diff_count)
    for v in S_diff_count.values():
        ans += v * (v - 1) // 2
    print(ans)
