def solve():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**20
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if i+1 in A and j+1 in A and k+1 in A:
                    x1,y1 = XY[i]
                    x2,y2 = XY[j]
                    x3,y3 = XY[k]
                    a = (x1-x2)**2 + (y1-y2)**2
                    b = (x2-x3)**2 + (y2-y3)**2
                    c = (x3-x1)**2 + (y3-y1)**2
                    ans = min(ans, max(a,b,c)**0.5)
    print(ans)

if __name__ == '__main__':
    solve()