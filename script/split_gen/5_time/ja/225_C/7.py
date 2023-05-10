def solve():
    N,M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    if N > 100:
        print('No')
        return
    if M > 7:
        print('No')
        return
    if M == 1:
        if N > 10:
            print('No')
            return
        if B[0][0] == 1 and B[1][0] == 2:
            print('Yes')
        else:
            print('No')
        return
    if N == 1:
        if M > 10:
            print('No')
            return
        if B[0][0] == 1 and B[0][1] == 2:
            print('Yes')
        else:
            print('No')
        return
    for i in range(N):
        for j in range(M):
            if B[i][j] != (i*7+j+1):
                print('No')
                return
    print('Yes')
    return
