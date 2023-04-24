Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = [0] * N
    for i in range(K):
        d = int(input())
        for j in map(int, input().split()):
            A[j - 1] += 1
    print(A.count(0))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [[] for _ in range(K)]
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        for j in range(d[i]):
            if A[i][j] not in A[i]:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    d = [0] * N
    for i in range(K):
        d_i = int(input())
        A = list(map(int, input().split()))
        for j in range(d_i):
            d[A[j]-1] += 1
    print(d.count(0))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    d = [0] * N
    for i in range(K):
        a = list(map(int, input().split()))
        for j in range(a[0]):
            d[a[j + 1] - 1] += 1
    print(d.count(0))

=======
Suggestion 5

def main():
    #input
    N, K = map(int, input().split())
    d = [int(input()) for _ in range(K)]
    A = [list(map(int, input().split())) for _ in range(K)]
    #compute
    ans = 0
    for i in range(K):
        for j in range(d[i]):
            if A[i][j] == 1:
                ans += 1
    #output
    print(N-ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = set()
    for _ in range(K):
        d = int(input())
        for a in map(int, input().split()):
            S.add(a)
    print(N - len(S))

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    s = set()
    for i in range(k):
        d = int(input())
        for j in input().split():
            s.add(j)
    print(n - len(s))

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    snacks = set()
    for i in range(k):
        d = int(input())
        snacks.update(map(int, input().split()))
    print(n - len(snacks))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(list(map(int, input().split())))
    d = [j for i in d for j in i]
    d = set(d)
    print(N - len(d))

=======
Suggestion 10

def main():
    #input
    n, k = map(int, input().split())
    d = [0] * k
    a = [[] for _ in range(k)]
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))

    #compute
    ans = 0
    for i in range(1, n+1):
        for j in range(k):
            if i in a[j]:
                ans += 1
                break

    #output
    print(n-ans)
