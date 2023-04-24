Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(k):
        ans += (p[i] + 1) / 2
    now = ans
    for i in range(k, n):
        now += (p[i] + 1) / 2 - (p[i - k] + 1) / 2
        ans = max(ans, now)
    print(ans)

main()

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = 0.0
    for i in range(K):
        ans += (P[i] + 1) / 2
    tmp = ans
    for i in range(N - K):
        tmp += (P[i + K] + 1) / 2 - (P[i] + 1) / 2
        ans = max(ans, tmp)
    print(ans)
    return 0

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(k):
        ans += (p[i]+1)/2
    tmp = ans
    for i in range(k,n):
        tmp -= (p[i-k]+1)/2
        tmp += (p[i]+1)/2
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    P = [0] * (N + 1)
    for i in range(N):
        P[i + 1] = P[i] + p[i]
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, (P[i + K] - P[i]) / 2 + P[i])
    print(ans)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0.0
    for i in range(N-K+1):
        ans = max(ans, sum(p[i:i+K])/K)
    print(ans)
    return 0

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    sum_P = sum(P[:K])
    max_sum_P = sum_P
    for i in range(K, N):
        sum_P += P[i] - P[i - K]
        max_sum_P = max(max_sum_P, sum_P)
    print((max_sum_P + K) / 2)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(N-K+1):
        if i == 0:
            ans += sum(p[i:i+K]) / K
        else:
            ans = max(ans,ans + (p[i+K-1] - p[i-1]) / K)
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    #print(N, K, p)
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, sum(p[i:i+K])/2+0.5*K)
    print(ans)

=======
Suggestion 9

def calc_expectation(n, k, p):
    expectation = 0
    for i in range(k):
        expectation += (p[i] + 1) / 2
    max_expectation = expectation
    for i in range(k, n):
        expectation += (p[i] + 1) / 2
        expectation -= (p[i - k] + 1) / 2
        if expectation > max_expectation:
            max_expectation = expectation
    return max_expectation


n, k = map(int, input().split())
p = list(map(int, input().split()))
print(calc_expectation(n, k, p))

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    #print(N, K, P)

    # 期待値の最大化は、積の最大化と同じ
    # つまり、積の最大化は、対数の和の最大化と同じ
    # つまり、対数の和の最大化は、K個の連続する要素の和の最大化と同じ

    # K個の連続する要素の和の最大化は、K個の連続する要素の和の最大化と同じ
    # つまり、K個の連続する要素の和の最大化は、K個の連続する要素の和の最大化と同じ
    # つまり、K個の連続する要素の和の最大化は、K個の連続する要素の和の最大化と同じ
    # つまり、K個の連続する要素の和の最大化は、K個の連続する要素の和の最大化と同じ
    # つまり、K個の連続する要素の和の最大化は、K個の連続する要素の和の最大化と同じ
    # つまり、K個の連続する要素の和の最大化は、K個の連続する要素の和の最大化と同じ
    # つまり、K個の連続する要素の和の最大化は、K個の連続する要素の和の最大化と同じ
    # つまり、K個の連続する要素の和の最大化は、K個の連続する要素の和の最大化と同じ
    # つまり、K個の連続する要素の和の最大
