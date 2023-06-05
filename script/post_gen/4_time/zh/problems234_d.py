Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K-1, N):
        print(sorted(P[:i+1])[-K+1])

=======
Suggestion 2

def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(k-1, n):
        print(sorted(p[0:i+1])[-k+1])

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    for i in range(k-1,n):
        print(sorted(p[:i+1])[-k])
main()

=======
Suggestion 4

def solve():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    for i in range(K,N+1):
        print(sorted(P[:i])[-K])

=======
Suggestion 5

def solve():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))

    #print(N,K,P)
    for i in range(K-1,N):
        print(sorted(P[:i+1])[-K])

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(k-1, n):
        print(sorted(p[:i+1])[-k+1])

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))

    # 遍历p，找到前k个最大值，存入res
    res = []
    for i in range(k-1,n):
        max = p[i]
        for j in range(i-k+1,i):
            if max < p[j]:
                max = p[j]
        res.append(max)

    # 输出res
    for i in range(len(res)):
        print(res[i])

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    p = [int(i) for i in input().split()]
    for i in range(k,n+1):
        print(sorted(p[:i])[-k])
