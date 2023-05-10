Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K, P)
    #print(N, K, P)
    #print(sorted(P))
    #print(sorted(P)[K-1])
    #print(sorted(P)[K-1:])

    for i in range(N-K+1):
        print(sorted(P)[K-1:][i])

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = []
    for i in range(N-K+1):
        ans.append(sorted(P[i:i+K])[-2])
    print(*ans, sep='\n')

=======
Suggestion 3

def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))

    # 1 2 3 4 5 6 7 8 9 10 11
    # 3 7 2 5 11 6 1 9 8 10  4
    # 1 2 3 4 5 6 7 8 9 10 11
    # 6 2 7 3 1 5 11 9 8 10  4
    # 1 2 3 4 5 6 7 8 9 10 11
    # 6 2 7 3 1 5 11 9 8 10  4
    # 1 2 3 4 5 6 7 8 9 10 11
    # 6 2 7 3 1 5 11 9 8 10  4
    # 1 2 3 4 5 6 7 8 9 10 11
    # 6 2 7 3 1 5 11 9 8 10  4
    # 1 2 3 4 5 6 7 8 9 10 11
    # 6 2 7 3 1 5 11 9 8 10  4
    # 1 2 3 4 5 6 7 8 9 10 11
    # 6 2 7 3 1 5 11 9 8 10  4
    # 1 2 3 4 5 6 7 8 9 10 11

    # 1 2 3 4 5 6 7 8 9 10 11
    # 3 7 2 5 11 6 1 9 8 10  4
    # 1 2 3 4 5 6 7 8 9 10 11
    # 6 2 7 3 1 5 11 9

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    #print("Q:", Q)
    for i in range(K - 1, N):
        print(Q[i])

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    ans = []
    for i in range(n-k+1):
        ans.append(sorted(p[i:i+k])[k-1])
    print(*ans,sep="\n")

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    print(p)
    for i in range(k-1, n):
        print(p[i-k+1:i+1])

=======
Suggestion 7

def main():
    N,K=map(int,input().split())
    P=list(map(int,input().split()))
    p=P[:K]
    p.sort()
    for i in range(K,N):
        p.append(P[i])
        p.sort()
        p.pop(0)
        print(p[0])

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K)
    #print(P)
    #print(sorted(P))
    #print(sorted(P)[K-1:N])
    for i in range(K, N+1):
        print(sorted(P)[K-1:N][i-K])

=======
Suggestion 9

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # print(N, K)
    # print(P)
    # print(sorted(P))
    # print(sorted(P)[K-1])
    for i in range(N-K+1):
        print(sorted(P[i:i+K])[K-1])

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + p[i]
    ans = 0
    for i in range(k, n + 1):
        ans = max(ans, s[i] - s[i - k])
    print(ans)
