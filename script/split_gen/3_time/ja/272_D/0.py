def main():
    N, M = map(int, input().split())
    ans = [[-1] * N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ans[i][j] == -1:
                continue
            for k in range(N):
                for l in range(N):
                    if (k - i) ** 2 + (l - j) ** 2 == M:
                        if ans[k][l] == -1:
                            ans[k][l] = ans[i][j] + 1
                        else:
                            ans[k][l] = min(ans[k][l], ans[i][j] + 1)
    for i in range(N):
        print(" ".join(map(str, ans[i])))
