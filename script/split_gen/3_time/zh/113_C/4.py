def main():
    N, M = map(int, input().split())
    city = []
    for i in range(M):
        P, Y = map(int, input().split())
        city.append([i, P, Y])
    city.sort(key=lambda x: x[2])
    city.sort(key=lambda x: x[1])
    #print(city)
    #for i in range(M):
    #    print(city[i][0], city[i][1], city[i][2])
    ans = [0] * M
    count = [0] * (N + 1)
    for i in range(M):
        count[city[i][1]] += 1
        ans[city[i][0]] = str(city[i][1]).zfill(6) + str(count[city[i][1]]).zfill(6)
    for i in range(M):
        print(ans[i])
