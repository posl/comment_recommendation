def main():
    N = int(input())
    tlr = []
    for _ in range(N):
        tlr.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr[i][0] == 1:
                l1 = tlr[i][1]
                r1 = tlr[i][2]
            elif tlr[i][0] == 2:
                l1 = tlr[i][1]
                r1 = tlr[i][2] - 1
            elif tlr[i][0] == 3:
                l1 = tlr[i][1] + 1
                r1 = tlr[i][2]
            elif tlr[i][0] == 4:
                l1 = tlr[i][1] + 1
                r1 = tlr[i][2] - 1
            if tlr[j][0] == 1:
                l2 = tlr[j][1]
                r2 = tlr[j][2]
            elif tlr[j][0] == 2:
                l2 = tlr[j][1]
                r2 = tlr[j][2] - 1
            elif tlr[j][0] == 3:
                l2 = tlr[j][1] + 1
                r2 = tlr[j][2]
            elif tlr[j][0] == 4:
                l2 = tlr[j][1] + 1
                r2 = tlr[j][2] - 1
            if r1 < l2 or r2 < l1:
                continue
            else:
                ans += 1
    print(ans)
