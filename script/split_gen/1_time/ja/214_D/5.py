def main():
    N = int(input())
    edge = []
    for i in range(N-1):
        u,v,w = map(int,input().split())
        edge.append([u,v,w])
    edge.sort(key=lambda x:x[2])
    ans = 0
    for i in range(N-1):
        ans += (N-i-1)*edge[i][2]
    print(ans)
