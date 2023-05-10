def main():
    N,X,Y = map(int,input().split())
    U = []
    V = []
    for i in range(N-1):
        u,v = map(int,input().split())
        U.append(u)
        V.append(v)
    ans = [0]*(N-1)
    for i in range(N-1):
        for j in range(i+1,N):
            if i+1 == j:
                continue
            if U[i] == X and V[i] == Y and U[j] == X and V[j] == Y:
                ans[i] += 1
                ans[j] += 1
            elif U[i] == X and V[i] == Y:
                ans[i] += 1
            elif U[j] == X and V[j] == Y:
                ans[j] += 1
            elif U[i] == X and U[j] == Y:
                ans[i] += 1
                ans[j] += 1
            elif U[i] == Y and U[j] == X:
                ans[i] += 1
                ans[j] += 1
            elif V[i] == X and V[j] == Y:
                ans[i] += 1
                ans[j] += 1
            elif V[i] == Y and V[j] == X:
                ans[i] += 1
                ans[j] += 1
    for i in range(N-1):
        print(ans[i])

if __name__ == '__main__':
    main()