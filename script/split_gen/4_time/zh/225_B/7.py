def solve():
    N = int(input())
    edges = []
    for i in range(N-1):
        a, b = map(int, input().split())
        edges.append((a, b))
    edges.sort()
    if edges[0][0] == 1:
        print('Yes')
    else:
        print('No')
