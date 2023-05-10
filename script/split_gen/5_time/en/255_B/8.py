def main():
    N,K = map(int,input().split())
    A = sorted(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(N)]
    X = [x for x,y in XY]
    Y = [y for x,y in XY]
    ans = 10**10
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                a = A.index(i+1)
                b = A.index(j+1)
                c = A.index(k+1)
                x1 = max(X[a],X[b],X[c])
                x2 = min(X[a],X[b],X[c])
                y1 = max(Y[a],Y[b],Y[c])
                y2 = min(Y[a],Y[b],Y[c])
                ans = min(ans,(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    print(ans**0.5)
