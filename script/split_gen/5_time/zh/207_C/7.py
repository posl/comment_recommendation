def solve():
    N = int(input())
    TLR = []
    for i in range(N):
        t, l, r = map(int, input().split())
        TLR.append([t, l, r])
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if TLR[i][0] == 1 or TLR[i][0] == 3:
                if TLR[j][0] == 1 or TLR[j][0] == 2:
                    if TLR[i][1] <= TLR[j][1] <= TLR[i][2]:
                        ans += 1
                if TLR[j][0] == 3 or TLR[j][0] == 4:
                    if TLR[i][1] <= TLR[j][1] < TLR[i][2]:
                        ans += 1
            if TLR[i][0] == 2 or TLR[i][0] == 4:
                if TLR[j][0] == 1 or TLR[j][0] == 2:
                    if TLR[i][1] < TLR[j][1] <= TLR[i][2]:
                        ans += 1
                if TLR[j][0] == 3 or TLR[j][0] == 4:
                    if TLR[i][1] < TLR[j][1] < TLR[i][2]:
                        ans += 1
    print(ans)
