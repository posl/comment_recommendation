def main():
    N, X = map(int, input().split())
    V = [0] * N
    P = [0] * N
    for i in range(N):
        V[i], P[i] = map(int, input().split())
    alcohol = 0
    for i in range(N):
        alcohol += V[i] * P[i] / 100
        if alcohol > X:
            print(i + 1)
            return
    print(-1)
    return

if __name__ == '__main__':
    main()