def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += not (tlr[j][1] <= tlr[i][1] and tlr[i][2] <= tlr[j][2]) and \
                not (tlr[j][1] >= tlr[i][2] or tlr[i][1] >= tlr[j][2]) and \
                not (tlr[j][1] == tlr[i][1] and tlr[i][2] == tlr[j][2] and tlr[i][0] == 1 and tlr[j][0] == 1) and \
                not (tlr[j][1] == tlr[i][1] and tlr[i][2] == tlr[j][2] and tlr[i][0] == 2 and tlr[j][0] == 2) and \
                not (tlr[j][1] == tlr[i][1] and tlr[i][2] == tlr[j][2] and tlr[i][0] == 3 and tlr[j][0] == 3) and \
                not (tlr[j][1] == tlr[i][1] and tlr[i][2] == tlr[j][2] and tlr[i][0] == 4 and tlr[j][0] == 4)
    print(ans)
