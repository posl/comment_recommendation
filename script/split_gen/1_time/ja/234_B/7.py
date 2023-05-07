def main():
    N = int(input())
    XY = [list(map(int,input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans,((XY[i][0]-XY[j][0])**2+(XY[i][1]-XY[j][1])**2)**0.5)
    print(ans)
