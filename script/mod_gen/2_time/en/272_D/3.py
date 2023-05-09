def main():
    N, M = map(int, input().split())
    ans = [[-1]*N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ans[i][j] != -1:
                for k in range(1, int(M**0.5)+1):
                    if i+k < N and ans[i+k][j] == -1:
                        ans[i+k][j] = ans[i][j]+1
                    if i-k >= 0 and ans[i-k][j] == -1:
                        ans[i-k][j] = ans[i][j]+1
                    if j+k < N and ans[i][j+k] == -1:
                        ans[i][j+k] = ans[i][j]+1
                    if j-k >= 0 and ans[i][j-k] == -1:
                        ans[i][j-k] = ans[i][j]+1
    for i in range(N):
        print(" ".join(map(str, ans[i])))

if __name__ == '__main__':
    main()