Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))

    # 累積和
    s = [0]
    for i in range(N):
        s.append(s[-1] + (p[i] + 1) / 2)

    # 累積和の最大値
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, s[i + K] - s[i])

    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    s = [0] * n
    s[0] = (p[0] + 1) / 2
    for i in range(1, n):
        s[i] = s[i - 1] + (p[i] + 1) / 2
    ans = 0
    for i in range(n - k + 1):
        if i == 0:
            ans = max(ans, s[k - 1])
        else:
            ans = max(ans, s[i + k - 1] - s[i - 1])
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, sum(p[i:i+k]))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        if i == 0:
            tmp = sum([(p[j]+1)/2 for j in range(K)])
        else:
            tmp = tmp - (p[i-1]+1)/2 + (p[i+K-1]+1)/2
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [i*(i+1)/2/i for i in p]
    ans = sum(p[:K])
    tmp = ans
    for i in range(N-K):
        tmp = tmp-p[i]+p[i+K]
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    # 累積和
    cumsum = [0]
    for i in range(N):
        cumsum.append(cumsum[i] + (p[i] + 1) / 2)
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, cumsum[i + K] - cumsum[i])
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # P = [1, 2, 2, 4, 5]
    # K = 3
    # N = 5
    # print(P)
    # print(K)
    # print(N)
    # 期待値の計算
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 +

=======
Suggestion 8

def main():
    import sys
    readline = sys.stdin.readline
    import numpy as np

    N, K = map(int, readline().split())
    p = np.array(list(map(int, readline().split())))

    # 累積和
    s = np.cumsum(p)
    # 合計
    s = s[K:] - s[:-K]
    # 期待値
    e = (s + K) / 2

    print(np.max(e))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    # 1からp_iまでの目が等確率で出るサイコロの期待値を求める
    E = [0.5 * (i + 1) for i in p]
    # 期待値の累積和を求める
    for i in range(N):
        if i == 0:
            continue
        E[i] += E[i - 1]
    # 期待値の最大値を求める
    ans = 0
    for i in range(N - K + 1):
        if i == 0:
            ans = E[K - 1]
        else:
            ans = max(ans, E[i + K - 1] - E[i - 1])
    print(ans)

=======
Suggestion 10

def solve(N, K, p):
    p = [1 + x for x in p]
    s = sum(p[:K])
    m = s
    for i in range(N - K):
        s = s - p[i] + p[i + K]
        m = max(m, s)
    return m / 2

N, K = map(int, input().split())
p = list(map(int, input().split()))
print(solve(N, K, p))
