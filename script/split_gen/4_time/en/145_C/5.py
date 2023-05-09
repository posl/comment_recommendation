def main():
    N = int(input())
    town = []
    for i in range(N):
        x, y = map(int, input().split())
        town.append([x, y])
    path = [i for i in range(N)]
    count = 0
    for i in range(N):
        count += path[i]
    ans = 0
    for i in range(count):
        ans += ((town[path[0]][0] - town[path[1]][0]) ** 2 + (town[path[0]][1] - town[path[1]][1]) ** 2) ** 0.5
        for j in range(N - 2):
            ans += ((town[path[j + 1]][0] - town[path[j + 2]][0]) ** 2 + (town[path[j + 1]][1] - town[path[j + 2]][1]) ** 2) ** 0.5
        path = path[1:] + path[:1]
    ans = ans / (N * (N - 1) / 2)
    print(ans)
main()
