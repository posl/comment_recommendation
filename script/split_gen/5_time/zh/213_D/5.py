def main():
    N = int(input())
    road = [list(map(int, input().split())) for i in range(N-1)]
    road.sort()
    road = [[0, 0]] + road
    print(road)
    city = [0 for i in range(N+1)]
    city[1] = 1
    ans = [1]
    for i in range(1, N):
        if road[i][0] == 1:
            city[road[i][1]] = 1
            ans.append(road[i][1])
            continue
        if city[road[i][0]] == 1:
            city[road[i][1]] = 1
            ans.append(road[i][1])
        else:
            city[road[i][0]] = 1
            ans.append(road[i][0])
    for i in range(N-1):
        print(ans[i], end = " ")
    print(ans[N-1])
