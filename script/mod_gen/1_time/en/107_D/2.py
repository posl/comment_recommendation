def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append((A[i], i))
    B.sort()
    C = [0] * N
    for i in range(N):
        C[B[i][1]] = i
    D = [0] * N
    for i in range(N):
        D[i] = (C[i] + 1) * (N - C[i])
    E = []
    for i in range(N):
        E.append((D[i], B[i][0]))
    E.sort()
    print(E[N // 2][1])

if __name__ == '__main__':
    main()