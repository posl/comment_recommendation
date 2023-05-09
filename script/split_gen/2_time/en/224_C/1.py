def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (X[j]-X[i])*(Y[k]-Y[i]) != (X[k]-X[i])*(Y[j]-Y[i]):
                    ans += 1
    print(ans)
