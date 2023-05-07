def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    edges = list(reversed(edges))
    #print(edges)
    bridge = [0 for _ in range(n-1)]
    for edge in edges:
        a = edge[0]
        b = edge[1]
        if a > b:
            a, b = b, a
        bridge[a-1] = 1
        if a != b-1:
            bridge[b-2] = 1
    print(sum(bridge))
