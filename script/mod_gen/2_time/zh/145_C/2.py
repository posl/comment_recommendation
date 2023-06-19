def main():
    N = int(input())
    towns = []
    for i in range(N):
        x, y = map(int, input().split())
        towns.append((x, y))
    def dist(t1, t2):
        return ((t1[0]-t2[0])**2+(t1[1]-t2[1])**2)**0.5
    def dfs(towns, dists, town, d, used):
        if len(towns) == 0:
            return d
        else:
            min_d = float('inf')
            for i, t in enumerate(towns):
                d += dist(town, t)
                used[i] = True
                min_d = min(min_d, dfs(towns[:i]+towns[i+1:], dists, t, d, used))
                d -= dist(town, t)
                used[i] = False
            return min_d
    dists = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dists[i][j] = dist(towns[i], towns[j])
    used = [False]*N
    print(dfs(towns, dists, towns[0], 0, used))

if __name__ == '__main__':
    main()