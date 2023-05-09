def main():
    N = int(input())
    road = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)
    ans = []
    def dfs(now,pre):
        ans.append(now+1)
        for nxt in road[now]:
            if nxt == pre:
                continue
            dfs(nxt,now)
            ans.append(now+1)
    dfs(0,-1)
    print(*ans)

if __name__ == '__main__':
    main()