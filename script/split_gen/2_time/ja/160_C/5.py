def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    #print(K, N, A)
    dist = [0] * N
    for i in range(N):
        dist[i] = A[i] - A[i-1]
    dist[0] = K - A[N-1] + A[0]
    #print(dist)
    print(K - max(dist))
