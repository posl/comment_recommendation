def main():
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    S = 0
    for i in range(N):
        S += V[i] * P[i]
        if S > X * 100:
            print(i + 1)
            return
    print(-1)

if __name__ == '__main__':
    main()