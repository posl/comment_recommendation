def main():
    N=int(input())
    xyP = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans, abs(xyP[i][0]-xyP[j][0])+abs(xyP[i][1]-xyP[j][1]))
    print(ans)
