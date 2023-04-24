Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N - i, K - i) + 1):
            tmp = V[:i] + V[N - j:]
            tmp.sort()
            tmp = tmp[:K - i - j]
            ans = max(ans, sum(tmp))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            v = V[:i] + V[N - j:]
            v.sort()
            ans = max(ans, sum(v[max(0, K - i - j):]))
    print(ans)

=======
Suggestion 3

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
            for k in range(min(i + j, K - i - j)):
                if tmp[k] < 0:
                    tmp[k] = 0
            ans = max(ans, sum(tmp))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for a in range(min(N, K) + 1):
        for b in range(min(N - a, K - a) + 1):
            tmp = V[:a] + V[N - b:]
            tmp.sort()
            for i in range(K - a - b):
                if len(tmp) == 0:
                    break
                if tmp[0] > 0:
                    break
                tmp.pop(0)
            ans = max(ans, sum(tmp))
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K)+1):
        for j in range(min(N-i, K-i)+1):
            tmp = sorted(V[:i]+V[N-j:])
            tmp = tmp[:K-i-j]
            tmp = sum(tmp)
            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(min(n, k) + 1):
        for j in range(min(n, k) - i + 1):
            if i + j == 0:
                continue
            tmp = sorted(v[:i] + v[n - j:])
            for l in range(min(i + j, k - i - j)):
                if tmp[l] < 0:
                    tmp[l] = 0
            ans = max(ans, sum(tmp))
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for left in range(min(N, K) + 1):
        for right in range(min(N, K) - left + 1):
            gems = V[:left] + V[N - right:]
            gems.sort()
            tmp = sum(gems)
            for i in range(min(left + right, K - left - right)):
                if gems[i] < 0:
                    tmp -= gems[i]
                else:
                    break
            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(N+1):
        for j in range(N-i+1):
            if i+j > K:
                break
            tmp = V[:i] + V[N-j:]
            tmp.sort()
            for k in range(K-(i+j)):
                if k >= len(tmp) or tmp[k] >= 0:
                    break
                tmp[k] = 0
            ans = max(ans, sum(tmp))
    print(ans)

=======
Suggestion 9

def main():
    #入力
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    #解答
    ans = 0
    for i in range(K+1):
        for j in range(K+1-i):
            if i+j > N:
                continue
            tmp = V[:i] + V[-j:]
            tmp.sort()
            for k in range(K-i-j):
                if len(tmp) == 0:
                    break
                if tmp[0] < 0:
                    tmp.pop(0)
                else:
                    break
            ans = max(ans, sum(tmp))
    print(ans)
