Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    max_d = 0
    for i in range(N):
        if i == 0:
            max_d = K - A[N-1] + A[0]
        else:
            max_d = max(max_d, A[i]-A[i-1])
    print(K-max_d)

=======
Suggestion 2

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))

    max_distance = 0
    for i in range(n):
        if i == n - 1:
            distance = k - a[i] + a[0]
        else:
            distance = a[i + 1] - a[i]

        if distance > max_distance:
            max_distance = distance

    print(k - max_distance)

=======
Suggestion 3

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K + A[0])
    d = [A[i + 1] - A[i] for i in range(N)]
    print(K - max(d))

=======
Suggestion 4

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    ans = K + min(A[0] + K - A[-1], *[A[i] - A[i-1] for i in range(1, N)])
    print(ans)

=======
Suggestion 5

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    max_d = 0
    for i in range(n):
        d = a[i+1]-a[i]
        if d > max_d:
            max_d = d
    print(k-max_d)

=======
Suggestion 6

def solve():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    print(K - max(A[i + 1] - A[i] for i in range(N)))

=======
Suggestion 7

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        if i == 0:
            B.append(K - A[i] + A[i + 1])
        elif i == N - 1:
            B.append(K - A[i] + A[0])
        else:
            B.append(A[i + 1] - A[i])
    print(K - max(B))
main()

=======
Suggestion 8

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(k)
    a.append(a[0] + k)
    a.sort()
    max = 0
    for i in range(n):
        if a[i+1] - a[i] > max:
            max = a[i+1] - a[i]
    print(k - max)

=======
Suggestion 9

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    max_distance = 0
    for i in range(N):
        max_distance = max(max_distance, A[i+1] - A[i])
    print(K - max_distance)

=======
Suggestion 10

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    max_dist = 0
    for i in range(n):
        max_dist = max(max_dist, a[i+1]-a[i])
    print(k-max_dist)
