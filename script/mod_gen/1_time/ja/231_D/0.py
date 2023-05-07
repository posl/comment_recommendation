def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A = sorted(A)
    B = sorted(B)
    print("Yes" if A[M - 1] < B[0] else "No")

if __name__ == '__main__':
    main()