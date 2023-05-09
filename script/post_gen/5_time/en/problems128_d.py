Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            A = V[:i] + V[N - j:]
            A.sort()
            tmp = sum(A)
            for k in range(min(K - i - j, i + j)):
                if A[k] < 0:
                    tmp -= A[k]
            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N,K)+1):
        for j in range(min(N,K)-i+1):
            l = V[:i] + V[N-j:]
            l.sort()
            ans = max(ans, sum(l[max(0,K-i-j):]))
    print(ans)

main()

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0
    for i in range(min(N, K)+1):
        for j in range(min(N, K)-i+1):
            jewels = V[:i] + V[N-j:]
            jewels.sort()
            for k in range(min(K-i-j, len(jewels))):
                if jewels[k] < 0:
                    jewels[k] = 0
            ans = max(ans, sum(jewels))
    print(ans)

main()

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(K, N) + 1):
        for r in range(min(K, N) - l + 1):
            if l + r > N:
                continue
            A = sorted(V[:l] + V[N - r:])
            ans = max(ans, sum(A[max(0, K - l - r):]))
    print(ans)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N,K)+1):
        for j in range(min(N,K)-i+1):
            t = V[:i] + V[N-j:]
            t.sort()
            for k in range(min(K-i-j, len(t))):
                if t[k] < 0:
                    t[k] = 0
            ans = max(ans, sum(t))
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    result = 0
    for l in range(min(K, N)+1):
        for r in range(min(K, N)-l+1):
            if l+r > N:
                continue
            if l+r > K:
                continue
            tmp = V[:l] + V[N-r:]
            tmp.sort()
            result = max(result, sum(tmp[K-l-r:]))
    print(result)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    k = min(n, k)
    for i in range(k+1):
        for j in range(k+1-i):
            l = v[:i] + v[n-j:]
            l.sort()
            ans = max(ans, sum(l[j:]))
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    K = min(K, N)

    ans = 0

    for i in range(K+1):
        for j in range(K+1-i):
            l = V[:i]
            r = V[N-j:]
            lr = sorted(l + r)
            m = K-i-j
            ans = max(ans, sum(lr[m:]))
    print(ans)

=======
Suggestion 9

def solve(n,k,vs):
    ans = 0
    for i in range(min(n+1,k+1)):
        for j in range(min(n+1-i,k+1-i)):
            l = vs[:i]
            r = vs[n-j:]
            l.extend(r)
            l.sort()
            for x in range(min(len(l),k-i-j)):
                if l[x] < 0:
                    l[x] = 0
            ans = max(ans,sum(l))
    return ans

=======
Suggestion 10

def problems128_d():
    pass
