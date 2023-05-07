def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    dist = [0] * (N-1)
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            dist[min(j-i, abs(X-i)+1+abs(j-Y))] += 1
    for i in range(1, N):
        print(dist[i])
