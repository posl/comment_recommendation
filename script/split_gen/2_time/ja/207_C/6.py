def main():
    N = int(input())
    l = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if l[i][0] == 1:
                if l[j][0] == 1:
                    if l[i][1] <= l[j][1] <= l[i][2]:
                        ans += 1
                    if l[i][1] <= l[j][2] <= l[i][2]:
                        ans += 1
                elif l[j][0] == 2:
                    if l[i][1] <= l[j][1] <= l[i][2]:
                        ans += 1
                elif l[j][0] == 3:
                    if l[i][1] <= l[j][2] <= l[i][2]:
                        ans += 1
                elif l[j][0] == 4:
                    if l[i][1] <= l[j][1] <= l[i][2]:
                        ans += 1
                    if l[i][1] <= l[j][2] <= l[i][2]:
                        ans += 1
            elif l[i][0] == 2:
                if l[j][0] == 1:
                    if l[i][1] <= l[j][1] <= l[i][2]:
                        ans += 1
                elif l[j][0] == 2:
                    if l[i][1] < l[j][1] < l[i][2]:
                        ans += 1
                    if l[i][1] < l[j][2] < l[i][2]:
                        ans += 1
                elif l[j][0] == 3:
                    if l[i][1] < l[j][2] < l[i][2]:
                        ans += 1
                elif l[j][0] == 4:
                    if l[i][1] < l[j][1] < l[i][2]:
                        ans += 1
                    if l[i][1] < l[j][2] < l[i][2]:
                        ans += 1
            elif l[i][0] == 3:
                if l[j][0] == 1:
                    if l[i][1] <= l[j][2] <= l[i][2
