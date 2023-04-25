Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = [A[i + 1] - A[i] for i in range(N - 1)]
    B.append(K - A[-1] + A[0])
    print(K - max(B))

=======
Suggestion 2

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    dist = []
    for i in range(N - 1):
        dist.append(A[i + 1] - A[i])
    dist.append(K - A[N - 1] + A[0])

    print(K - max(dist))

=======
Suggestion 3

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    ans = 0
    for i in range(N):
        ans = max(ans, A[i + 1] - A[i])
    print(K - ans)

=======
Suggestion 4

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    d = []
    for i in range(N):
        d.append(A[i+1] - A[i])
    print(K - max(d))

=======
Suggestion 5

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    D = [A[i + 1] - A[i] for i in range(N)]
    print(K - max(D))

=======
Suggestion 6

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    dis = [A[i + 1] - A[i] for i in range(N)]
    print(K - max(dis))

=======
Suggestion 7

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    #print(K, N)
    #print(A)
    max_dist = 0
    for i in range(N-1):
        max_dist = max(max_dist, A[i+1] - A[i])
    max_dist = max(max_dist, K - A[N-1] + A[0])
    #print(max_dist)
    print(K - max_dist)

=======
Suggestion 8

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    #print(K, N)
    #print(A)
    dist = [0] * N
    for i in range(N-1):
        dist[i] = A[i+1] - A[i]
    dist[N-1] = K - A[N-1] + A[0]
    #print(dist)
    print(K - max(dist))

=======
Suggestion 9

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    # 一番遠い家と一番近い家の距離を求める
    max_dist = 0
    for i in range(N - 1):
        dist = A[i + 1] - A[i]
        max_dist = max(max_dist, dist)

    # 一番遠い家と一番近い家の距離のうち、一周した場合の距離を考慮する
    dist = K - A[-1] + A[0]
    max_dist = max(max_dist, dist)

    # 一番遠い家と一番近い家の距離のうち、一番遠い家から一番近い家に向かう距離を求める
    print(K - max_dist)

=======
Suggestion 10

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    # The minimum distance to travel is the largest distance between two houses.
    # If we sort the distances in ascending order, the largest distance is the difference between the last and first houses.
    # If the pond is circular, the distance between the first and last houses is K minus the difference between the last and first houses.
    # Therefore, the minimum distance to travel is the maximum of the difference between the last and first houses and K minus the difference between the last and first houses.
    # If there are only two houses, the minimum distance to travel is the difference between the last and first houses.
    if N == 2:
        print(A[1] - A[0])
    else:
        A.append(A[0] + K)
        B = [A[i + 1] - A[i] for i in range(N)]
        print(max(max(B), K - min(B)))
