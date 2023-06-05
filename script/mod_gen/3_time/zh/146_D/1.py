def main():
    N = int(input())
    
    # 邻接表
    graph = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        graph[a - 1].append((b - 1, i))
        graph[b - 1].append((a - 1, i))
    
    # 求解
    color = [-1] * (N - 1)
    used = [False] * N
    used[0] = True
    k = 0
    stack = [(0, -1, 0)]
    while stack:
        v, p, c = stack.pop()
        k = max(k, c + 1)
        cnt = 0
        for u, i in graph[v]:
            if used[u]:
                continue
            cnt += 1
            if cnt == c:
                cnt += 1
            color[i] = cnt
            used[u] = True
            stack.append((u, v, cnt))
    print(k)
    for c in color:
        print(c)

if __name__ == '__main__':
    main()