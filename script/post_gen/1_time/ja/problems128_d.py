Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N - i, K - i) + 1):
            if i + j == 0:
                continue
            v = V[:i] + V[N - j:]
            v.sort()
            for k in range(min(K - i - j, len(v))):
                if v[k] < 0:
                    v[k] = 0
                else:
                    break
            ans = max(ans, sum(v))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            if i + j > K:
                continue
            tmp = sorted(V[:i] + V[N - j:])
            tmp_sum = sum(tmp)
            for k in range(min(i + j, len(tmp))):
                if tmp[k] >= 0:
                    break
                tmp_sum -= tmp[k]
            ans = max(ans, tmp_sum)
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N - i, K - i) + 1):
            tmp = V[:i] + V[N - j:]
            tmp.sort()
            ans = max(ans, sum(tmp[max(0, K - i - j):]))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N - i, K - i) + 1):
            if i + j == 0:
                continue
            A = V[:i]
            B = V[N - j:]
            C = sorted(A + B)
            ans = max(ans, sum(C[max(0, i + j - K):]))
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for a in range(min(N, K) + 1):
        for b in range(min(N, K) - a + 1):
            T = V[:a] + V[N - b:]
            T.sort()
            s = sum(T)
            for i in range(min(K - a - b, len(T))):
                if T[i] < 0:
                    s -= T[i]
                else:
                    break
            ans = max(ans, s)
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) + 1):
            if i + j > K:
                continue
            if i + j > N:
                continue
            tmp = sum(V[:i]) + sum(V[-j:])
            tmp = sorted(tmp)
            tmp = tmp[min(i + j, K)]
            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0
    for i in range(K + 1):
        for j in range(K + 1 - i):
            if i + j > N:
                continue
            tmp = V[:i] + V[N - j:]
            tmp.sort()
            for k in range(K - i - j):
                if k < len(tmp) and tmp[k] < 0:
                    tmp[k] = 0
                else:
                    break
            ans = max(ans, sum(tmp))

    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0
    for i in range(K + 1):
        for j in range(K - i + 1):
            if i + j > N:
                continue
            tmp = V[:i] + V[N-j:]
            tmp.sort()
            ans = max(ans, sum(tmp[max(0, i + j - K):]))
    print(ans)

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    V = list(map(int,input().split()))
    ans = 0
    for i in range(min(N,K)+1):
        for j in range(min(N,K)-i+1):
            tmp = V[:i] + V[N-j:]
            tmp.sort()
            if i+j <= K:
                ans = max(ans,sum(tmp[:K-(i+j)]))
            else:
                ans = max(ans,sum(tmp))
    print(ans)

=======
Suggestion 10

def main():
    #入力
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    
    #計算
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) + 1):
            if i + j > K or i + j > N:
                continue
            w = V[:i] + V[N - j:]
            w.sort()
            w = w[:K - i - j]
            ans = max(ans, sum(w) + i + j)
    
    #出力
    print(ans)
