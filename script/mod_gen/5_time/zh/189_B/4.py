def main():
    N,X = map(int,input().split())
    V = []
    P = []
    for i in range(N):
        v,p = map(int,input().split())
        V.append(v)
        P.append(p)
    V = [V[i]*P[i]/100 for i in range(N)]
    V = [sum(V[:i+1]) for i in range(N)]
    if V[-1] <= X:
        print(-1)
    else:
        for i in range(N):
            if V[i] > X:
                print(i+1)
                break

if __name__ == '__main__':
    main()