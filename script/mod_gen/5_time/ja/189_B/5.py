def main():
    N, X = map(int, input().split())
    V, P = [], []
    for _ in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    a = 0
    for i in range(N):
        a += V[i] * P[i]
        if a > X * 100:
            print(i + 1)
            return
    print(-1)

if __name__ == '__main__':
    main()