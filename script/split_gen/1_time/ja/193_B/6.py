def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a,p,x = map(int,input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    ans = 1000000000
    for i in range(N):
        if X[i] > 0:
            ans = min(ans,P[i])
    if ans == 1000000000:
        print(-1)
    else:
        print(ans)
