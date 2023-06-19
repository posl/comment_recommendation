def main():
    N,M = map(int, input().split())
    city = [list(map(int, input().split())) for i in range(M)]
    city = sorted(city, key=lambda x:x[1])
    cnt = 0
    ans = [0]*M
    for i in range(M):
        if i == 0:
            cnt += 1
            ans[i] = str(city[i][0]).zfill(6)+str(cnt).zfill(6)
        else:
            if city[i-1][0] == city[i][0]:
                cnt += 1
                ans[i] = str(city[i][0]).zfill(6)+str(cnt).zfill(6)
            else:
                cnt = 1
                ans[i] = str(city[i][0]).zfill(6)+str(cnt).zfill(6)
    for i in range(M):
        print(ans[i])
