def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [a for a, b in sorted(zip(A, B), reverse=True)]
    B = [b for a, b in sorted(zip(A, B), reverse=True)]
    C = [a + b for a, b in zip(A, B)]
    C = [c for c, a, b in sorted(zip(C, A, B), reverse=True)]
    for i in range(N):
        if i < X:
            print(i + 1)
        elif i >= X and i < X + Y:
            if B[i] > C[X - 1]:
                print(i + 1)
        elif i >= X + Y:
            if A[i] + B[i] > C[X + Y - 1]:
                print(i + 1)

if __name__ == '__main__':
    main()