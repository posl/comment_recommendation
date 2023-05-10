def main():
    N = int(input())
    A = [list(map(int, input())) for i in range(N)]
    ans = -1
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                continue
            tmp = 0
            for k in range(N):
                for l in range(N):
                    tmp += min(abs(i-k), abs(j-l)) * A[k][l]
            ans = max(ans, tmp)
    print(ans)
