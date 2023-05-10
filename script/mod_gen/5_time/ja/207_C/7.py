def main():
    n = int(input())
    tlr = []
    for i in range(n):
        tlr.append(list(map(int, input().split())))
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if tlr[i][0] == 1:
                if tlr[j][0] == 1:
                    if tlr[i][1] <= tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] <= tlr[j][2] <= tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][1] <= tlr[j][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][2] <= tlr[j][2]:
                        ans += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] <= tlr[j][2] <= tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][1] < tlr[j][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][2] <= tlr[j][2]:
                        ans += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] <= tlr[j][2] <= tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] < tlr[i][1] <= tlr[j][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][2] <= tlr[j][2]:
                        ans += 1
                elif tlr[j][0] == 4:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] < tlr[j][2] < t

if __name__ == '__main__':
    main()