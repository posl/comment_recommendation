def main():
    n, m = map(int, input().split())
    road = []
    for i in range(m):
        a, b = map(int, input().split())
        road.append([a, b])
    for i in range(1, n+1):
        ans = []
        for j in range(m):
            if i in road[j]:
                ans.append(road[j][0]) if road[j][1] == i else ans.append(road[j][1])
        ans.sort()
        ans.insert(0, len(ans))
        print(*ans)
