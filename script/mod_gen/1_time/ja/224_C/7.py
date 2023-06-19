def main():
    N = int(input())
    x = []
    y = []
    for _ in range(N):
        X, Y = map(int, input().split())
        x.append(X)
        y.append(Y)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if (x[j]-x[i])*(y[k]-y[i]) != (x[k]-x[i])*(y[j]-y[i]):
                    cnt += 1
    print(cnt)
main()
