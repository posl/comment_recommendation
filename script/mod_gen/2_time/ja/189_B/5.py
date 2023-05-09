def main():
    N, X = map(int, input().split())
    V = [0] * N
    P = [0] * N
    for i in range(N):
        V[i], P[i] = map(int, input().split())
    for i in range(N):
        X -= V[i] * P[i] / 100
        if X < 0:
            print(i + 1)
            return
    print(-1)

if __name__ == '__main__':
    main()