def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    ans = [-1] * N
    ans[0] = 0
    stack = [(0, 0)]
    while stack:
        v, par = stack.pop()
        for nv in graph[v]:
            if ans[nv] != -1:
                continue
            ans[nv] = v
            stack.append((nv, v))
    if -1 in ans[1:]:
        print('No')
    else:
        print('Yes')
        for a in ans[1:]:
            print(a + 1)
