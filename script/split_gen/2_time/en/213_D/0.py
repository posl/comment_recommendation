def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    ans = [0]
    stack = [0]
    while len(stack) > 0:
        v = stack[-1]
        if len(graph[v]) > 0:
            next_v = graph[v].pop()
            stack.append(next_v)
            ans.append(next_v)
            ans.append(v)
        else:
            stack.pop()
    print(*[x + 1 for x in ans])
