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
