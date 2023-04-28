Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    ans = K - (A[-1] - A[0])
    for i in range(N-1):
        ans = max(ans, A[i+1] - A[i])
    print(K - ans)
    return

=======
Suggestion 2

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    max_distance = 0
    for i in range(N-1):
        max_distance = max(max_distance, A[i+1]-A[i])
    max_distance = max(max_distance, K-A[N-1]+A[0])
    print(K-max_distance)

=======
Suggestion 3

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    ans = K
    for i in range(N):
        ans = min(ans, A[i + 1] - A[i])
    print(ans)

=======
Suggestion 4

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    max_distance = 0
    for i in range(N):
        if i == N - 1:
            distance = K - A[i] + A[0]
        else:
            distance = A[i + 1] - A[i]
        if distance > max_distance:
            max_distance = distance
    print(K - max_distance)

=======
Suggestion 5

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    max_dist = 0
    for i in range(N):
        if i == N-1:
            dist = K - A[i] + A[0]
        else:
            dist = A[i+1] - A[i]
        if dist > max_dist:
            max_dist = dist
    print(K - max_dist)

=======
Suggestion 6

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    ans = k
    for i in range(n):
        ans = min(ans, k-(a[i+1]-a[i]))
    print(ans)

=======
Suggestion 7

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    max = 0
    for i in range(n):
        if max < a[i+1] - a[i]:
            max = a[i+1] - a[i]
    print(k - max)

=======
Suggestion 8

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K)
    d = []
    for i in range(N):
        d.append(A[i+1]-A[i])
    d.append(K-A[N]+A[0])
    print(K-max(d))

=======
Suggestion 9

def solve():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K + A[0])
    print(K - max([A[i + 1] - A[i] for i in range(N)]))
solve()

=======
Suggestion 10

def main():
    k,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(k+a[0])
    max_dis = 0
    for i in range(n):
        if max_dis < a[i+1]-a[i]:
            max_dis = a[i+1]-a[i]
    print(k-max_dis)
