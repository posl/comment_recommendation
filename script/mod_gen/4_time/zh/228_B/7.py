def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, X)
    # print(A)
    B = [0] * N
    B[X - 1] = 1
    # print(B)
    for i in range(N):
        if B[i] == 1:
            B[A[i] - 1] = 1
    print(sum(B))

if __name__ == '__main__':
    main()