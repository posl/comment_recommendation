def main():
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for i in range(M)]
    city.sort(key=lambda x: x[1])
    # print(city)
    ans = [0] * M
    cnt = [0] * N
    for i in range(M):
        p, y = city[i]
        cnt[p - 1] += 1
        ans[i] = [p, cnt[p - 1]]
    ans.sort(key=lambda x: x[1])
    # print(ans)
    for i in range(M):
        print(str(ans[i][0]).zfill(6) + str(ans[i][1]).zfill(6))
