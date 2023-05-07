def main():
    N = int(input())
    graph = [[] for i in range(N)]
    for i in range(N-1):
        u, v, w = map(int, input().split())
        graph[u-1].append([v-1, w])
        graph[v-1].append([u-1, w])
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        node = stack.pop()
        for i, w in graph[node]:
            if color[i] == -1:
                color[i] = (color[node] + w) % 2
                stack.append(i)
    for i in color:
        print(i)
main()
