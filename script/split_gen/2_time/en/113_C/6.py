def main():
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(M)]
    city.sort(key=lambda x: x[1])
    cnt = [0] * (N+1)
    for i in range(M):
        cnt[city[i][0]] += 1
        city[i].append(cnt[city[i][0]])
    city.sort(key=lambda x: x[0])
    for i in range(M):
        print(str(city[i][0]).zfill(6) + str(city[i][2]).zfill(6))
