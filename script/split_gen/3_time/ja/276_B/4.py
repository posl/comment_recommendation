def main():
    N,M=map(int,input().split())
    road=[[] for _ in range(N)]
    for _ in range(M):
        a,b=map(int,input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)
    for i in range(N):
        road[i].sort()
        print(len(road[i]),end=" ")
        for j in road[i]:
            print(j+1,end=" ")
        print()
