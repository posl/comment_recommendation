def main():
    N,X = map(int,input().split())
    V = []
    P = []
    for i in range(N):
        v,p = map(int,input().split())
        V.append(v)
        P.append(p)
    total = 0
    for i in range(N):
        total += V[i] * P[i] / 100
        if total > X:
            print(i+1)
            exit()
    print(-1)

if __name__ == '__main__':
    main()