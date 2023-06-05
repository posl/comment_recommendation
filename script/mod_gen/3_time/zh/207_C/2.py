def main():
    n = int(input())
    tlr = []
    for i in range(n):
        tlr.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if tlr[i][0] == 1 or tlr[i][0] == 2:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] <= tlr[i][2] or tlr[i][1] <= tlr[j][2] <= tlr[i][2]:
                        ans += 1
                else:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2] or tlr[i][1] < tlr[j][2] <= tlr[i][2]:
                        ans += 1
            else:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2] or tlr[i][1] <= tlr[j][2] < tlr[i][2]:
                        ans += 1
                else:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2] or tlr[i][1] < tlr[j][2] < tlr[i][2]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()