Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n-1):
        b.append(a[i+1] - a[i])
    b.append(k - a[-1] + a[0])
    print(sum(b) - max(b))

=======
Suggestion 2

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))

    dist = [a[i + 1] - a[i] for i in range(n - 1)]
    dist.append(k - a[-1] + a[0])

    print(k - max(dist))

=======
Suggestion 3

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    d = []
    for i in range(n):
        d.append(a[i+1]-a[i])
    print(k-max(d))

=======
Suggestion 4

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(k+a[0])
    d = [a[i+1]-a[i] for i in range(n)]
    print(k - max(d))

=======
Suggestion 5

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    D = [A[i+1]-A[i] for i in range(N-1)]
    D.append(K - A[-1] + A[0])
    print(K - max(D))

=======
Suggestion 6

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    diff = [A[i]-A[i-1] for i in range(1, N)]
    diff.append(K-A[N-1]+A[0])
    print(K-max(diff))

=======
Suggestion 7

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0] + k)
    for i in range(n):
        a[i] = a[i+1] - a[i]
    print(k - max(a))

=======
Suggestion 8

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0]+K)
    A.sort()
    dist = 0
    for i in range(N):
        dist = max(dist, A[i+1]-A[i])
    print(K-dist)

=======
Suggestion 9

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    a.sort()
    print(k-max([a[i+1]-a[i] for i in range(n)]))

=======
Suggestion 10

def getDistance(a, b, k):
    if a > b:
        a, b = b, a
    return min(b - a, a + k - b)
