Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    S = sorted(P[:K])
    print(S[K - 1])
    for i in range(K, N):
        S.remove(P[i - K])
        S.insert(bisect.bisect_left(S, P[i]), P[i])
        print(S[K - 1])

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    S = sorted(P[:K])
    print(S[K-1])
    for i in range(K, N):
        S.append(P[i])
        S.sort()
        print(S[K-1])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    for i in range(K, N):
        print(P[i-K])

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    for i in range(K, N):
        print(P[i])

main()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K, N):
        if P[i] > P[i-K]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    S = sorted(P[:K])
    for i in range(N - K):
        print(S[K - 1])
        S.remove(P[i])
        S.insert(bisect.bisect_left(S, P[i + K]), P[i + K])
    print(S[K - 1])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K)
    #print(P)
    for i in range(K, N+1):
        #print(i)
        #print(P[i-K:i])
        print(sorted(P[i-K:i])[-2])

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = []
    for i in range(K, N):
        ans.append(str(min(P[i-K:i+1])))
    print('

'.join(ans))

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    psum = [0] * (n + 1)
    for i in range(1, n + 1):
        psum[i] = psum[i - 1] + p[i]
    ans = []
    for i in range(k, n + 1):
        ans.append((psum[i] - psum[i - k]) / k)
    print(*ans, sep='

')

main()

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [x-K for x in P]
    P = [max(0, x) for x in P]
    s = sum(P[:K])
    print(s)
    for i in range(N-K):
        s = s + P[K+i] - P[i]
        print(s)

main()
