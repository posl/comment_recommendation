def main():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr[i][0] == 1 or tlr[i][0] == 2:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] and tlr[i][2] >= tlr[j][1]:
                        count += 1
                else:
                    if tlr[i][1] <= tlr[j][1] and tlr[i][2] > tlr[j][1]:
                        count += 1
            else:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] and tlr[i][2] >= tlr[j][1]:
                        count += 1
                else:
                    if tlr[i][1] < tlr[j][1] and tlr[i][2] > tlr[j][1]:
                        count += 1
    print(count)

if __name__ == '__main__':
    main()