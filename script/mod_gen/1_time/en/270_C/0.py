def main():
    N, X, Y = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = [0] * N
    for i in range(N):
        visited = [False] * N
        queue = [i]
        dist = 0
        while queue:
            dist += 1
            next_queue = []
            for j in queue:
                visited[j] = True
                for k in G[j]:
                    if not visited[k]:
                        next_queue.append(k)
                        ans[k] += dist
            queue = next_queue
    for i in range(N):
        if i == X-1 or i == Y-1:
            continue
        print(ans[i])
main()

if __name__ == '__main__':
    main()