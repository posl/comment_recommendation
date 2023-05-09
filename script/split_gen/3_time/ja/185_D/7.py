def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N + 1]
    dist = []
    for i in range(M + 1):
        dist.append(A[i + 1] - A[i] - 1)
    max_dist = max(dist)
    if max_dist == 0:
        print(0)
    else:
        print(max_dist - dist.count(max_dist) + 1)
