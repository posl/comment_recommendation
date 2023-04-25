Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P_cum = [0]
    for p in P:
        P_cum.append(P_cum[-1] + p)
    ans = 0
    for i in range(K, N+1):
        ans = max(ans, (P_cum[i] - P_cum[i-K]) / 2 + P_cum[i-K])
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    s = [0] * (N + 1)
    for i in range(1, N + 1):
        s[i] = s[i - 1] + p[i]
    ans = 0
    for i in range(K, N + 1):
        ans = max(ans, s[i] - s[i - K])
    print((ans + K) / 2)

=======
Suggestion 3

def problems154_d():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    ans = 0
    for i in range(K):
        ans += (p[N-i-1] + 1) / 2
    print(ans)

=======
Suggestion 4

def dice():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        ans += p[i]
    tmp = ans
    for i in range(K, N):
        tmp += p[i] - p[i-K]
        ans = max(ans, tmp)
    print((ans+K)/2)

dice()

=======
Suggestion 5

def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))

    ans = 0
    tmp = sum(p[:k])
    ans = max(ans, tmp)
    for i in range(n-k):
        tmp += p[i+k] - p[i]
        ans = max(ans, tmp)
    print((ans+k)/2)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p

    sum_p = [0]
    for i in range(1, N+1):
        sum_p.append(sum_p[i-1] + p[i])

    max_expect = 0
    for i in range(N-K+1):
        expect = (sum_p[i+K] - sum_p[i]) / 2 + p[i+K]
        if max_expect < expect:
            max_expect = expect

    print(max_expect)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [x/2 for x in p]
    s = sum(p[:K])
    max_s = s
    for i in range(N-K):
        s = s - p[i] + p[i+K]
        max_s = max(max_s, s)
    print(max_s)

=======
Suggestion 8

def dice(n,k,p):
    sum = 0
    for i in range(0,k):
        sum += p[i]
    max = sum
    for i in range(k,n):
        sum += p[i]
        sum -= p[i-k]
        if sum > max:
            max = sum
    return max

n,k = map(int,input().split())
p = list(map(int,input().split()))
max = dice(n,k,p)
print((max+k)/2)

=======
Suggestion 9

def dice(n,k,p):
    max_sum = 0
    for i in range(0, n-k+1):
        sum = 0
        for j in range(i, i+k):
            sum += p[j]
        max_sum = max(max_sum, sum)
    return max_sum/2.0

n, k = map(int, input().split())
p = list(map(int, input().split()))
print(dice(n,k,p))

=======
Suggestion 10

def dice(dice, k):
    if k == 1:
        return max(dice)
    else:
        return max(dice) + dice(dice[1:], k-1)

n, k = map(int, input().split())
dice = list(map(int, input().split()))

print(dice(dice, k)/2)
