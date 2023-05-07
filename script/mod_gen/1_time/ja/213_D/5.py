def main():
    N = int(input())
    roads = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        roads[a-1].append(b-1)
        roads[b-1].append(a-1)
    ans = [0]
    def dfs(before, now):
        for i in roads[now]:
            if i == before:
                continue
            ans.append(i)
            dfs(now, i)
            ans.append(now)
    dfs(0, 0)
    print(' '.join(map(str, [i+1 for i in ans])))

if __name__ == '__main__':
    main()