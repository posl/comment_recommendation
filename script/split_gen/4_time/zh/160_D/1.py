def main():
    N,X,Y = map(int,input().split())
    dist = [0]*N
    for i in range(1,N):
        for j in range(i+1,N+1):
            dist[min(abs(i-j),abs(X-i)+1+abs(Y-j),abs(Y-i)+1+abs(X-j))] += 1
    for i in range(1,N):
        print(dist[i])
