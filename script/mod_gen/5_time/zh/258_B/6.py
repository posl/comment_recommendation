def main():
    n = int(input())
    A = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        A[i] = list(map(int, input()))
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(8):
                ni, nj = i, j
                for l in range(n-1):
                    ni += dx[k]
                    nj += dy[k]
                    if ni == n:
                        ni = 0
                    if nj == n:
                        nj = 0
                    ans = max(ans, A[ni][nj])
    print(ans)
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
main()
