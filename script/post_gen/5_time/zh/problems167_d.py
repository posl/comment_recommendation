Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    i = 0
    while b[i] == 0:
        b[i] = 1
        i = a[i] - 1
    c = []
    while b[i] == 1:
        c.append(i)
        b[i] = 2
        i = a[i] - 1
    d = c.index(i)
    if k < d:
        print(c[k] + 1)
    else:
        print(c[(k - d) % (len(c) - d) + d] + 1)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    count = 0
    while True:
        count += 1
        i = A[i] - 1
        if count == K:
            print(i + 1)
            break

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    town = 1
    for i in range(K):
        town = A[town - 1]
    print(town)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    [N,K] = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    count = 0
    while count < K:
        count += 1
        A = [A[ai-1] for ai in A]
    print(A[0])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    for j in range(K):
        i = A[i] - 1
    print(i + 1)

=======
Suggestion 7

def readinput():
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,k,a

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [0] * N
    visited[0] = 1
    i = 0
    while K > 0:
        i = A[i] - 1
        K -= 1
        if visited[i] == 1:
            break
        visited[i] = 1
    if K == 0:
        print(i + 1)
    else:
        K %= sum(visited)
        while K > 0:
            i = A[i] - 1
            K -= 1
        print(i + 1)

solve()

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k = k % n
    for i in range(k):
        a = [a[i-1] for i in a]
    print(a[0])
