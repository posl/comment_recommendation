def main():
    n = int(input())
    tlr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if tlr[i][0] == 1:
                if tlr[j][0] == 1:
                    if tlr[i][1] <= tlr[j][1] <= tlr[i][2]:
                        cnt += 1
                    elif tlr[j][1] <= tlr[i][1] <= tlr[j][2]:
                        cnt += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2]:
                        cnt += 1
                    elif tlr[j][1] < tlr[i][1] <= tlr[j][2]:
                        cnt += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        cnt += 1
                    elif tlr[j][1] <= tlr[i][1] < tlr[j][2]:
                        cnt += 1
                else:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                        cnt += 1
                    elif tlr[j][1] < tlr[i][1] < tlr[j][2]:
                        cnt += 1
            elif tlr[i][0] == 2:
                if tlr[j][0] == 1:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        cnt += 1
                    elif tlr[j][1] <= tlr[i][1] < tlr[j][2]:
                        cnt += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                        cnt += 1
                    elif tlr[j][1] < tlr[i][1] < tlr[j][2]:
                        cnt += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][1

if __name__ == '__main__':
    main()