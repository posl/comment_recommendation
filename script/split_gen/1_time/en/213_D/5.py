def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    road = [[] for _ in range(n+1)]
    for a, b in ab:
        road[a].append(b)
        road[b].append(a)
    for i in range(n+1):
        road[i].sort()
    ans = []
    stack = [1]
    while stack:
        now = stack.pop()
        ans.append(now)
        for next in road[now]:
            if next not in ans:
                stack.append(next)
    print(*ans)
