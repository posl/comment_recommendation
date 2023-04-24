Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            if i + j > N:
                continue
            tmp = sorted(V[:i] + V[N - j:], reverse=True)
            for k in range(min(K - i - j, len(tmp))):
                if tmp[k] < 0:
                    tmp[k] = 0
            ans = max(ans, sum(tmp))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) + 1):
            if i + j > K or i + j > N:
                continue
            tmp = V[:i] + V[N - j:]
            tmp.sort()
            ans = max(ans, sum(tmp[max(0, i + j - K):]))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(K, N) + 1):
        for j in range(min(K - i, N) + 1):
            if i + j == 0:
                continue
            tmp = V[:i] + V[N-j:]
            tmp.sort()
            for k in range(min(K - i - j, i + j)):
                if tmp[k] >= 0:
                    break
                tmp[k] = 0
            ans = max(ans, sum(tmp))
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for a in range(min(n, k) + 1):
        for b in range(min(n, k) - a + 1):
            now = v[:a] + v[n - b:]
            now.sort()
            for i in range(k - a - b):
                if i == len(now) or now[i] > 0:
                    break
                now[i] = 0
            ans = max(ans, sum(now))
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N - i, K - i) + 1):
            v = V[:i] + V[N - j:]
            v.sort()
            ans = max(ans, sum(v) + sum([0] + v[:K - i - j] if v[:K - i - j] else [0]))

    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(K+1):
        for j in range(K-i+1):
            if i + j > N:
                continue
            tmp = V[:i] + V[N-j:]
            tmp.sort()
            for k in range(K-i-j):
                if len(tmp) <= k or tmp[k] >= 0:
                    break
                tmp[k] = 0
            ans = max(ans, sum(tmp))
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(K+1, N+1)):
        for j in range(min(K-i+1, N-i+1)):
            tmp = 0
            tmpV = []
            for k in range(i):
                tmp += V[k]
                tmpV.append(V[k])
            for k in range(j):
                tmp += V[N-1-k]
                tmpV.append(V[N-1-k])
            tmpV.sort()
            for k in range(K-i-j):
                if tmpV[k] >= 0:
                    break
                tmp -= tmpV[k]
            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0

    for i in range(min(N, K) + 1):
        for j in range(min(N, K) + 1):
            if i + j > K:
                continue
            tmp = V[:i] + V[N - j:]
            tmp.sort()
            ans = max(ans, sum(tmp[min(i + j, K - i - j):]))

    print(ans)

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    V = list(map(int,input().split()))
    ans = 0
    for i in range(min(N,K)+1):
        for j in range(min(N,K)-i+1):
            tmp = 0
            for k in range(i):
                tmp += V[k]
            for k in range(j):
                tmp += V[N-1-k]
            tmp += max(0,K-i-j)
            ans = max(ans,tmp)
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    Vs = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) + 1):
            if i + j > K:
                continue
            if i + j > N:
                continue
            tmp = Vs[:i] + Vs[N - j:]
            tmp.sort()
            tmp = tmp[:K - i - j]
            ans = max(ans, sum(tmp))
    print(ans)
