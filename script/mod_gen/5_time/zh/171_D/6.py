def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    # Q = int(input())
    # BC = [list(map(int, input().split())) for _ in range(Q)]
    N = 4
    A = [1, 2, 3, 4]
    Q = 3
    BC = [[1, 2], [3, 4], [2, 4]]
    for i in range(Q):
        for j in range(N):
            if A[j] == BC[i][0]:
                A[j] = BC[i][1]
        print(sum(A))
    # print(A)

if __name__ == '__main__':
    main()