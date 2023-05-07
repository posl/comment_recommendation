def main():
    N, M = map(int, input().split())
    road = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        road[a].append(b)
        road[b].append(a)
    ans = 0
    for i in range(len(road[1])):
        if N in road[road[1][i]]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()