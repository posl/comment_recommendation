def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    D = sorted(range(N), key=lambda x: (A[x], B[x], C[x], x), reverse=True)
    E = D[:X] + D[X:X+Y] + D[X+Y:X+Y+Z]
    print(*sorted(E), sep='
')

if __name__ == '__main__':
    main()