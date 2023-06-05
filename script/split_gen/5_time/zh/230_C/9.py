def printGrid(N, A, B, P, Q, R, S):
    # 1. 先把所有格子都填上.，再把需要涂黑的格子填上#
    grid = [['.' for col in range(S-R+1)] for row in range(Q-P+1)]
    # 2. 涂黑(A+k,B+k)和(A+k,B-k)两个点
    for k in range(max(1-A,1-B), min(N-A,N-B)+1):
        grid[A+k-P][B+k-R] = '#'
    for k in range(max(1-A,B-N), min(N-A,B-1)+1):
        grid[A+k-P][B-k-R] = '#'
    # 3. 输出
    for row in grid:
        print(''.join(row))
