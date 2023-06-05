def main():
    # N M C = map(int, input().split())
    # B = list(map(int, input().split()))
    # A = [list(map(int, input().split())) for _ in range(N)]
    N = 5
    M = 2
    C = -4
    B = [-2, 5]
    A = [[100, 41], [100, 40], [-3, 0], [-6, -2], [18, -13]]
    count = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j] * B[j]
        sum += C
        if sum > 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()