Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        ans += (p[i] + 1) / 2
    tmp = ans
    for i in range(N - K):
        tmp -= (p[i] + 1) / 2
        tmp += (p[i + K] + 1) / 2
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        ans += (p[i]+1)/2
    tmp = ans
    for i in range(N-K):
        tmp = tmp - (p[i]+1)/2 + (p[i+K]+1)/2
        ans = max(ans, tmp)
    print(ans)
main()

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    s = 0
    for i in range(K):
        s += (p[i] + 1) / 2
    ans = s
    for i in range(K, N):
        s += (p[i] + 1) / 2 - (p[i - K] + 1) / 2
        ans = max(ans, s)
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:k])
    m = s
    for i in range(n - k):
        s -= p[i]
        s += p[i + k]
        m = max(m, s)
    print((m + k) / 2)

main()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    s = 0
    for i in range(K):
        s += p[i]
    m = s
    for i in range(K, N):
        s += p[i] - p[i - K]
        m = max(m, s)
    print(m / 2 + K / 2)

main()

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    c = [0] * (N + 1)
    for i in range(N):
        c[i + 1] = c[i] + (p[i] + 1) / 2
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, c[i + K] - c[i])
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [i * (i + 1) / 2 / i for i in p]
    print(max(sum(p[i: i + K]) for i in range(N - K + 1)))

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    sum_p = 0
    for i in range(K):
        sum_p += (p[i]+1)/2
    max_p = sum_p
    for i in range(K,N):
        sum_p += (p[i]+1)/2 - (p[i-K]+1)/2
        max_p = max(max_p,sum_p)
    print(max_p)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K, P)
    sum = 0
    for i in range(K):
        sum += (P[i] + 1) / 2
    max = sum
    for i in range(N - K):
        sum -= (P[i] + 1) / 2
        sum += (P[i + K] + 1) / 2
        if sum > max:
            max = sum
    print(max)

=======
Suggestion 10

def main():
    N, K = map(int, input().split(' '))
    p = list(map(int, input().split(' ')))
    p = [i+1 for i in p]
    p = [i/2 for i in p]
    ans = sum(p[0:K])
    tmp = ans
    for i in range(N-K):
        tmp = tmp - p[i] + p[i+K]
        if tmp > ans:
            ans = tmp
    print(ans)
