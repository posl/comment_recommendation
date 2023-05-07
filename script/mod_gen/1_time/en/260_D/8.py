def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    eaten = [False] * N
    eatable = [False] * N
    eatable[N - 1] = True
    for i in range(N - 2, -1, -1):
        if P[i] < P[i + 1]:
            eatable[i] = True
        else:
            eatable[i] = False
    for i in range(N):
        if eatable[i]:
            for j in range(i, i + K):
                eaten[j] = True
    for i in range(N):
        if eaten[i]:
            print(P[i])
        else:
            print(-1)

if __name__ == '__main__':
    main()