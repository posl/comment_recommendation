Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    dist = []
    for i in range(N-1):
        dist.append(A[i+1] - A[i])
    dist.append(K + A[0] - A[N-1])
    print(K - max(dist))

=======
Suggestion 2

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - 1):
        ans = max(ans, A[i + 1] - A[i])
    ans = max(ans, K - A[-1] + A[0])
    print(K - ans)

=======
Suggestion 3

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    distance = []
    for i in range(N - 1):
        distance.append(A[i + 1] - A[i])
    distance.append(A[0] + K - A[N - 1])

    print(K - max(distance))

=======
Suggestion 4

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    d = [A[i + 1] - A[i] for i in range(N)]
    print(sum(d) - max(d))

=======
Suggestion 5

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K + A[0])
    D = [A[i + 1] - A[i] for i in range(N)]
    print(K - max(D))

=======
Suggestion 6

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0]+K)
    dist = [A[i+1]-A[i] for i in range(N)]
    print(K-max(dist))

=======
Suggestion 7

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A = A + [A[0] + K]
    dist = []
    for i in range(N):
        dist.append(A[i + 1] - A[i])
    print(K - max(dist))

=======
Suggestion 8

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    A.sort()
    print(min([K - (A[i + 1] - A[i]) for i in range(N)]))

=======
Suggestion 9

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    # Calculate the distance between houses
    dist = []
    dist.append(A[0] + K - A[N-1])
    for i in range(N-1):
        dist.append(A[i+1] - A[i])

    # Find the maximum distance
    dist.sort(reverse=True)
    ans = K - dist[0]
    print(ans)

=======
Suggestion 10

def main():
    # input
    K, N = map(int, input().split())
    As = list(map(int, input().split()))

    # compute
    # 1. compute the distance between the houses
    dists = [0] * N
    for i in range(N-1):
        dists[i] = As[i+1] - As[i]
    dists[N-1] = K - As[N-1] + As[0]
    # 2. compute the maximum distance
    max_dist = max(dists)

    # output
    print(K - max_dist)
