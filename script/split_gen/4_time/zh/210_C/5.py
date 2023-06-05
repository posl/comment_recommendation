def solve():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    max_colors = 0
    colors = {}
    for i in range(K):
        if C[i] not in colors:
            colors[C[i]] = 1
        else:
            colors[C[i]] += 1
    max_colors = len(colors)
    for i in range(K, N):
        if C[i] not in colors:
            colors[C[i]] = 1
        else:
            colors[C[i]] += 1
        colors[C[i-K]] -= 1
        if colors[C[i-K]] == 0:
            del colors[C[i-K]]
        if len(colors) > max_colors:
            max_colors = len(colors)
    print(max_colors)
solve()
