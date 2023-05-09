def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    ans = 0
    for i in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    flag = [0] * N
    flag[0] = 1
    queue = [[0, 1]]
    while queue:
        now, cnt = queue.pop()
        if now == N-1:
            ans += cnt
            ans %= (10**9 + 7)
            continue
        for i in graph[now]:
            if flag[i] == 0:
                flag[i] = 1
                queue.append([i, cnt])
    print(ans)
