def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for i in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    for i in range(M):
        P[i] = str(P[i]).zfill(6)
        Y[i] = str(Y[i]).zfill(6)
    for i in range(M):
        print(P[i]+Y[i])

if __name__ == '__main__':
    main()