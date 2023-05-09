def main():
    n, q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    cd = [list(map(int, input().split())) for _ in range(q)]
    # graph[i] = [j, k, ...] means Town i is connected to Town j, k, ...
    graph = [[] for _ in range(n)]
    for a, b in ab:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    # dist[i] = j means Town i is j-th from Town 1
    dist = [-1] * n
    dist[0] = 0
    stack = [0]
    while stack:
        town = stack.pop()
        for next_town in graph[town]:
            if dist[next_town] == -1:
                dist[next_town] = dist[town] + 1
                stack.append(next_town)
    for c, d in cd:
        if (dist[c-1] + dist[d-1]) % 2 == 0:
            print('Town')
        else:
            print('Road')

if __name__ == '__main__':
    main()