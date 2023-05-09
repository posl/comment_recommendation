def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        a,b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    prev = [-1]*n
    prev[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if prev[nv] == -1:
                prev[nv] = v
                stack.append(nv)
    print(*[p+1 for p in prev])

if __name__ == '__main__':
    main()