def main():
    N = int(input())
    L = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i][0] == 1:
                if L[j][0] == 1:
                    if L[i][1] <= L[j][1] <= L[i][2]:
                        ans += 1
                    if L[j][1] <= L[i][1] <= L[j][2]:
                        ans += 1
                if L[j][0] == 2:
                    if L[i][1] <= L[j][1] <= L[i][2]:
                        ans += 1
                    if L[j][1] <= L[i][1] < L[j][2]:
                        ans += 1
                if L[j][0] == 3:
                    if L[i][1] < L[j][1] <= L[i][2]:
                        ans += 1
                    if L[j][1] <= L[i][1] <= L[j][2]:
                        ans += 1
                if L[j][0] == 4:
                    if L[i][1] < L[j][1] < L[i][2]:
                        ans += 1
                    if L[j][1] <= L[i][1] < L[j][2]:
                        ans += 1
            if L[i][0] == 2:
                if L[j][0] == 1:
                    if L[i][1] <= L[j][1] <= L[i][2]:
                        ans += 1
                    if L[j][1] <= L[i][1] < L[j][2]:
                        ans += 1
                if L[j][0] == 2:
                    if L[i][1] <= L[j][1] <= L[i][2]:
                        ans += 1
                    if L[j][1] < L[i][1] <= L[j][2]:
                        ans += 1
                if L[j][0] == 3:
                    if L[i][1] < L[j][1] <= L[i][2]:
                        ans += 1
                    if L[j][1] < L[i][1] <= L[j][2]:
                        ans += 1
