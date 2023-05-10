Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    total = sum(p[0:K])
    max_total = total
    for i in range(N-K):
        total = total - p[i] + p[i+K]
        if total > max_total:
            max_total = total
    print((max_total + K)/2)
main()

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    sum_p = [0] * (N+1)
    for i in range(1, N+1):
        sum_p[i] = sum_p[i-1] + p[i]

    ans = 0
    for i in range(1, N-K+2):
        ans = max(ans, (sum_p[i+K-1] - sum_p[i-1])/K)

    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        ans += (p[i]+1)*K/2
    tmp = ans
    for i in range(N-K):
        tmp -= (p[i]+1)*K/2
        tmp += (p[i+K]+1)*K/2
        ans = max(ans, tmp)
    print(ans)

main()

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))

    # 累積和をとる
    p_sum = [0] * (N + 1)
    for i in range(N):
        p_sum[i + 1] = p_sum[i] + p[i]

    # print(N, K)
    # print(p)
    # print(p_sum)

    # 期待値の最大値を求める
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, (p_sum[i + K] - p_sum[i]) / 2 + p_sum[i])

    print(ans)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    p_sum = sum(p[:k])
    max_p_sum = p_sum
    for i in range(n-k):
        p_sum = p_sum - p[i] + p[i+k]
        if p_sum > max_p_sum:
            max_p_sum = p_sum
    print((max_p_sum+k)/2)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    psum = [0] * (n+1)
    for i in range(n):
        psum[i+1] = psum[i] + p[i]
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, (psum[i+k] - psum[i] + k) / 2)
    print(ans)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(K):
        ans += (p[i]+1)/2
    tmp = ans
    for i in range(K,N):
        tmp = tmp - (p[i-K]+1)/2 + (p[i]+1)/2
        if ans < tmp:
            ans = tmp
    print(ans)
main()

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    
    #累積和を計算
    S = [0]
    for i in range(N):
        S.append(S[-1] + p[i])
    
    #K個選んだ時の期待値の最大値を求める
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, (S[i+K] - S[i])/2 + S[i])
    
    print(ans)

=======
Suggestion 9

def solve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p_sum = sum(p[:K])
    ans = p_sum
    for i in range(N-K):
        p_sum = p_sum - p[i] + p[i+K]
        if p_sum > ans:
            ans = p_sum
    print((ans+K)/2)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, sum(P[i:i + K]) / 2 + K / 2)
    print(ans)
