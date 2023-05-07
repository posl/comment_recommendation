def main():
    N, M = map(int, input().split())
    road = []
    for i in range(M):
        a, b = map(int, input().split())
        road.append([a, b])
    #print(road)
    road.sort(key=lambda x: x[0])
    #print(road)
    ans = []
    for i in range(N):
        ans.append(1)
    for i in range(M):
        if road[i][0] == 1:
            ans[road[i][1] - 1] = 1
    for i in range(M):
        if road[i][0] != 1:
            ans[road[i][1] - 1] = road[i][0]
    print("Yes")
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()