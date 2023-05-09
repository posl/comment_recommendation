def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    print(min(A[0] - 1, N - A[-1], B[0] - 1, N - B[-1]))

if __name__ == '__main__':
    main()