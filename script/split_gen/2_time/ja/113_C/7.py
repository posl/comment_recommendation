def problem113_c():
    N, M = map(int, input().split())
    city = [[0,0,0] for i in range(M)]
    for i in range(M):
        P, Y = map(int, input().split())
        city[i][0] = P
        city[i][1] = Y
        city[i][2] = i
    city.sort(key=lambda x:x[1])
    pref = [[0,0] for i in range(N)]
    ans = [0 for i in range(M)]
    for i in range(M):
        pref[city[i][0]-1][0] += 1
        pref[city[i][0]-1][1] += 1
        ans[city[i][2]] = str(city[i][0]).zfill(6) + str(pref[city[i][0]-1][1]).zfill(6)
    for i in range(M):
        print(ans[i])
problem113_c()
