Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p_sum = [0] * (N + 1)
    for i in range(N):
        p_sum[i + 1] = p_sum[i] + p[i]
    max_exp = 0
    for i in range(N - K + 1):
        exp = (p_sum[i + K] - p_sum[i]) / 2 + p_sum[i]
        if exp > max_exp:
            max_exp = exp
    print(max_exp)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    sum_p = [0] * (n+1)
    for i in range(n):
        sum_p[i+1] = sum_p[i] + p[i]
    max = 0
    for i in range(n-k+1):
        if max < sum_p[i+k] - sum_p[i]:
            max = sum_p[i+k] - sum_p[i]
    print((max + k) / 2)
main()

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p_sum = [0]
    for i in range(n):
        p_sum.append(p_sum[i] + p[i])
    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, p_sum[i + k] - p_sum[i])
    print((ans + k) / 2)

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    S = [0] * (N+1)
    for i in range(1, N+1):
        S[i] = S[i-1] + P[i-1]
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, (S[i+K]-S[i])/2)
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    for i in range(1, N+1):
        p[i] += p[i-1]
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, p[i+K] - p[i])
    print((ans + K) / 2)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        tmp = 0
        for j in range(i, i+K):
            tmp += (p[j]+1)/2
        if tmp > ans:
            ans = tmp
    print(ans)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    max_sum = 0
    for i in range(k):
        max_sum += (p[i] + 1) / 2
    temp_sum = max_sum
    for i in range(k, n):
        temp_sum = temp_sum - (p[i - k] + 1) / 2 + (p[i] + 1) / 2
        if temp_sum > max_sum:
            max_sum = temp_sum
    print(max_sum)

=======
Suggestion 8

def solve():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    for i in range(N):
        p[i] = (p[i]+1)/2
    s = sum(p[:K])
    ans = s
    for i in range(N-K):
        s -= p[i]
        s += p[i+K]
        ans = max(ans,s)
    print(ans)

=======
Suggestion 9

def solve(N, K, P):
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, sum(P[i:i+K])/K)
    return ans

=======
Suggestion 10

def main():
    #input
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    #compute
    sumP = [0] * (N + 1)
    for i in range(N):
        sumP[i + 1] = sumP[i] + P[i]

    ans = 0
    for i in range(K, N + 1):
        ans = max(ans, (sumP[i] - sumP[i - K]) / 2 + sumP[i - K])
    print(ans)
