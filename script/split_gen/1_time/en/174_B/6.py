def main():
    #input
    N, D = map(int, input().split())
    Xs = []
    Ys = []
    for i in range(N):
        X, Y = map(int, input().split())
        Xs.append(X)
        Ys.append(Y)
    #compute
    ans = 0
    for i in range(N):
        if (Xs[i]**2+Ys[i]**2)**(1/2) <= D:
            ans += 1
    #output
    print(ans)
main()
