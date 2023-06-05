def solve():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(8):
                ni = i
                nj = j
                for l in range(N):
                    ni += di[k]
                    nj += dj[k]
                    if ni < 0:
                        ni = N - 1
                    elif ni == N:
                        ni = 0
                    if nj < 0:
                        nj = N - 1
                    elif nj == N:
                        nj = 0
                    ans = max(ans, int(A[ni][nj]))
    print(ans)
di = [1, 1, 1, 0, -1, -1, -1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]
