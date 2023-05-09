def main():
    N, X = map(int, input().split())
    V, P = [], []
    for _ in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    total = 0
    for i in range(N):
        total += V[i] * P[i] / 100
        if total > X:
            print(i+1)
            return
    print(-1)
main()

if __name__ == '__main__':
    main()