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
