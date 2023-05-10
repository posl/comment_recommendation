def main():
    N,M = map(int,input().split())
    B = [list(map(int,input().split())) for i in range(N)]
    if N > 10000 or M > 7:
        return 0
    if N == 1 and M == 1:
        return 0
    if N == 1:
        for i in range(1,M):
            if B[0][i] - B[0][i-1] != 1:
                return 0
        return 1
    if M == 1:
        for i in range(1,N):
            if B[i][0] - B[i-1][0] != 7:
                return 0
        return 1
    if N == 2:
        for i in range(1,M):
            if B[0][i] - B[0][i-1] != 1:
                return 0
        for i in range(1,M):
            if B[1][i] - B[1][i-1] != 1:
                return 0
        if B[1][0] - B[0][0] != 7:
            return 0
        return 1
    if M == 2:
        for i in range(1,N):
            if B[i][0] - B[i-1][0] != 7:
                return 0
        for i in range(1,N):
            if B[i][1] - B[i-1][1] != 7:
                return 0
        if B[0][1] - B[0][0] != 1:
            return 0
        return 1
    for i in range(1,N):
        for j in range(1,M):
            if B[i][j] - B[i-1][j] != 7:
                return 0
            if B[i][j] - B[i][j-1] != 1:
                return 0
    return 1

if __name__ == '__main__':
    main()