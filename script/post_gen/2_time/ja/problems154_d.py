Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        ans += (p[i]+1)/2
    tmp = ans
    for i in range(K, N):
        tmp = tmp + (p[i]+1)/2 - (p[i-K]+1)/2
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(k):
        ans += (p[i]+1)/2
    tmp = ans
    for i in range(n-k):
        tmp -= (p[i]+1)/2
        tmp += (p[i+k]+1)/2
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))

    # 累積和
    s = [0]
    for i in range(N):
        s.append(s[i] + (p[i]+1)/2)

    # 累積和の差分
    d = []
    for i in range(N-K+1):
        d.append(s[i+K] - s[i])

    print(max(d))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(N):
        tmp += (p[i]+1)/2
        if i >= K:
            tmp -= (p[i-K]+1)/2
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    # 累積和
    s = [0] * (N+1)
    for i in range(1, N+1):
        s[i] = s[i-1] + (p[i-1] + 1) / 2
    # 最大値
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, s[i+K] - s[i])
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [i+1 for i in p]
    p = [i/2 for i in p]
    ans = sum(p[:k])
    tmp = ans
    for i in range(k, n):
        tmp += p[i] - p[i-k]
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(N-K+1):
        tmp = sum(p[i:i+K])
        if ans < tmp:
            ans = tmp
    print(ans+(K-1)/2)

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    #累積和
    p_sum = [0]
    for i in range(N):
        p_sum.append(p_sum[i] + (p[i]+1)/2)
    #print(p_sum)
    #最大値を求める
    max = 0
    for i in range(N-K+1):
        if max < p_sum[i+K]-p_sum[i]:
            max = p_sum[i+K]-p_sum[i]
    print(max)

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    Ps = list(map(int,input().split()))
    #累積和
    S = [0]
    for i in range(N):
        S.append(S[i]+Ps[i])
    #print(S)
    #期待値
    E = []
    for i in range(N-K+1):
        E.append((S[i+K]-S[i]+K)/2)
    print(max(E))

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    
    # 期待値を求める
    # 1からp[i]までのp[i]種類の目がそれぞれ等確率で出るので、
    # 期待値は(1+p[i])/2
    # つまり、期待値を求めるためには、1からp[i]までの和を求める必要がある。
    # これを累積和を用いて求める。
    for i in range(N):
        p[i] = (1+p[i]) / 2
    #print(p)
    # 累積和を求める
    for i in range(1, N):
        p[i] += p[i-1]
    #print(p)
    
    # 最大値を求める
    # 隣接するK個のサイコロを選んでそれぞれ独立に振ったとき、出る目の合計の期待値の最大値を求めるので、
    # K個のサイコロを選んでそれぞれ独立に振ったときの最大値を求める。
    # つまり、隣接するK個のサイコロを選んでそれぞれ独立に振ったときの最大値を求める。
    # つまり、隣接するK個のサイコロを選んでそれぞれ独立に振ったときの最大値を求める。
    # つまり、隣接するK個のサイコロを選んでそれぞれ独立に振ったときの最大値を求める。
    # つまり、隣接するK個のサイコロを選んでそれぞれ独
