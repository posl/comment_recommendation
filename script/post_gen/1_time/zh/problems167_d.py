Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    #print(A)
    #print(A[0], A[A[0]-1])
    i = 0
    k = 0
    while True:
        i = A[i] - 1
        k += 1
        if i == 0:
            break
        if k == K:
            break
    print(i+1)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [False] * N
    visited[0] = True
    i = 0
    for k in range(K):
        i = A[i] - 1
        if visited[i]:
            break
        visited[i] = True
    if k == K - 1:
        print(i + 1)
    else:
        K -= k
        K %= k
        for i in range(N):
            if visited[i]:
                K -= 1
                if K == 0:
                    print(i + 1)
                    break

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    i = 0
    count = 0
    while True:
        i = A[i]-1
        count += 1
        if i == 0:
            break
    K = K % count
    i = 0
    for j in range(K):
        i = A[i]-1
    print(i+1)

=======
Suggestion 5

def problem167_d():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * n
    B[0] = 1
    for i in range(n):
        if B[A[i]-1] == 0:
            B[A[i]-1] = 1
        else:
            break
    k = k % i
    for j in range(k):
        A = [A[a]-1 for a in range(n)]
    print(A[0]+1)

=======
Suggestion 6

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    visited = [False] * n
    visited[0] = True
    current = 0
    for i in range(k):
        current = a[current] - 1
        if visited[current]:
            break
        visited[current] = True
    if i == k - 1:
        print(current + 1)
    else:
        print(a[current])

=======
Suggestion 7

def f(n, k, a):
    if k <= n:
        return a[k-1]
    else:
        k = k % n
        if k == 0:
            return a[n-1]
        else:
            return a[k-1]

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = [0] * n
    d[0] = 1
    i = 0
    while True:
        i = a[i] - 1
        d[i] += 1
        if d[i] == 2:
            break
    for i in range(n):
        if d[i] == 2:
            break
    k %= d[i] - 1
    for _ in range(k):
        i = a[i] - 1
    print(i + 1)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    while (K > 0):
        K -= 1
        i = A[i] - 1
        if (i == 0):
            print(1)
            return
    print(i + 1)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    visited = [False]*n
    visited[0] = True
    count = 1
    next = a[0]-1
    while not visited[next]:
        visited[next] = True
        next = a[next]-1
        count += 1
    k = k%count
    next = 0
    while k>0:
        next = a[next]-1
        k -= 1
    print(next+1)
