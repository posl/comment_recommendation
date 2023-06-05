def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A + [0]
    B = [0] * (N + 2)
    C = [0] * (N + 2)
    D = [0] * (N + 2)
    E = [0] * (N + 2)
    for i in range(1, N + 1):
        B[i] = B[i - 1] + A[i]
    for i in range(1, N + 1):
        C[i] = C[i - 1] + A[i] * (-1) ** i
    for i in range(1, N + 1):
        D[i] = D[i - 1] + A[i] * (-1) ** (i + 1)
    for i in range(1, N + 1):
        E[i] = E[i - 1] + A[i] * (-1) ** i
    B.sort()
    C.sort()
    D.sort()
    E.sort()
    print(max(B[-1] - B[1], B[-2] - B[0], C[-1] - C[1], C[-2] - C[0], D[-1] - D[1], D[-2] - D[0], E[-1] - E[1], E[-2] - E[0]))

if __name__ == '__main__':
    main()