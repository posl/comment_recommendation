def main():
    N,M = map(int,input().split())
    ans = [[-1 for _ in range(N)] for _ in range(N)]
    ans[0][0] = 0
    if M == 1:
        for i in range(N):
            for j in range(N):
                ans[i][j] = i+j
    else:
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                if (i+j)**2 <= M:
                    ans[i][j] = (i+j)
                    continue
                for k in range(N):
                    for l in range(N):
                        if (i-k)**2+(j-l)**2 == M:
                            ans[i][j] = ans[k][l]+1
                            break
    for i in range(N):
        print(*ans[i])
