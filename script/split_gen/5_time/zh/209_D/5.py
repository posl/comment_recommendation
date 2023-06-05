def main():
    n, q = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for _ in range(q):
        c, d = map(int, input().split())
        if c == d:
            print('Town')
        else:
            if len(graph[c]) == 1 and len(graph[d]) == 1:
                print('Road')
            else:
                print('Town')
