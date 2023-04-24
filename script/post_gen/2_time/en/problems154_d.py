Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:k])
    m = s
    for i in range(n-k):
        s = s + p[k+i] - p[i]
        m = max(m, s)
    print(m/2+k/2)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:K])
    ma = s
    for i in range(N-K):
        s = s - p[i] + p[i+K]
        ma = max(ma, s)
    print((ma+K)/2)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:K])
    t = s
    for i in range(K, N):
        t = t - p[i-K] + p[i]
        s = max(s, t)
    print((s + K) / 2)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        if i == 0:
            ans = sum([x+1 for x in p[:K]])/K
        else:
            ans = max(ans, sum([x+1 for x in p[i:i+K]])/K)
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [i * (i + 1) / 2 / i for i in p]
    ans = sum(p[:K])
    tmp = ans
    for i in range(K, N):
        tmp += p[i] - p[i - K]
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [x + 1 for x in p]
    p = [x / 2 for x in p]
    p_sum = sum(p[:K])
    ans = p_sum
    for i in range(K, N):
        p_sum = p_sum - p[i - K] + p[i]
        ans = max(ans, p_sum)
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    E = [0] * (N - K + 1)
    for i in range(N - K + 1):
        E[i] = (p[i] + 1) / 2
        for j in range(1, K):
            E[i] += (p[i + j] + 1) / 2
    print(max(E))

main()

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [i+1 for i in p]
    p = [i/2 for i in p]
    ans = sum(p[:K])
    tmp = ans
    for i in range(N-K):
        tmp = tmp - p[i] + p[i+K]
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    max_exp = 0
    for i in range(N-K+1):
        exp = sum(p[i:i+K])/(K/2)
        if exp > max_exp:
            max_exp = exp
    print(max_exp)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    #print(N, K)
    #print(p)

    #print(sum(p[0:K]))
    #print(sum(p[0:K]) + sum(p[0:K]) - 1)
    #print(sum(p[0:K]) + sum(p[0:K]) - 1 + sum(p[0:K]) - 2)
    #print(sum(p[0:K]) + sum(p[0:K]) - 1 + sum(p[0:K]) - 2 + sum(p[0:K]) - 3)
    #print(sum(p[0:K]) + sum(p[0:K]) - 1 + sum(p[0:K]) - 2 + sum(p[0:K]) - 3 + sum(p[0:K]) - 4)
    #print(sum(p[0:K]) + sum(p[0:K]) - 1 + sum(p[0:K]) - 2 + sum(p[0:K]) - 3 + sum(p[0:K]) - 4 + sum(p[0:K]) - 5)

    #print(sum(p[0:K]) + sum(p[0:K]) - 1 + sum(p[0:K]) - 2 + sum(p[0:K]) - 3 + sum(p[0:K]) - 4 + sum(p[0:K]) - 5 + sum(p[0:K]) - 6)

    #print(sum(p[0:K]) + sum(p[0:K]) - 1 + sum(p[0:K]) - 2 + sum(p[0:K]) - 3 + sum(p[0:K]) - 4 + sum(p[0:K]) - 5 + sum(p[0:K]) - 6 + sum(p[0:K]) - 7)
    #print(sum(p[0:K]) + sum(p[0:K]) - 1 + sum(p[0:K]) - 2 + sum(p[0:K]) - 3 + sum(p[0:K]) - 4 + sum(p[0:K]) - 5 + sum(p
