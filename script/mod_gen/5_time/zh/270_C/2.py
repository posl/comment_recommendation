def main():
    N,X,Y = map(int,input().split())
    U = [0]*(N-1)
    V = [0]*(N-1)
    for i in range(N-1):
        U[i],V[i] = map(int,input().split())
    ans = []
    for i in range(N-1):
        if U[i] == X and V[i] == Y:
            ans.append(i)
        elif U[i] == Y and V[i] == X:
            ans.append(i)
    if len(ans) == 0:
        print(-1)
    else:
        print(ans[0])

if __name__ == '__main__':
    main()