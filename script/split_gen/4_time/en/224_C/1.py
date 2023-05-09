def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                a = X[j]-X[i]
                b = Y[j]-Y[i]
                c = X[k]-X[i]
                d = Y[k]-Y[i]
                if a*d != b*c:
                    ans += 1
    print(ans)
