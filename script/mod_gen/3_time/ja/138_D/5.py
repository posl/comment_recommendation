def main():
    import sys
    input = sys.stdin.readline
    from collections import deque
    N, Q = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
    counter = [0] * (N + 1)
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p] += x
    queue = deque([1])
    while queue:
        node = queue.pop()
        for child in graph[node]:
            counter[child] += counter[node]
            queue.append(child)
    print(*counter[1:])

if __name__ == '__main__':
    main()