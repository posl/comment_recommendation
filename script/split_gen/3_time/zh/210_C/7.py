def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    colors = {}
    for i in range(k):
        if c[i] not in colors:
            colors[c[i]] = 1
        else:
            colors[c[i]] += 1
    max_colors = len(colors)
    for i in range(k, n):
        if c[i] not in colors:
            colors[c[i]] = 1
        else:
            colors[c[i]] += 1
        if colors[c[i-k]] == 1:
            del colors[c[i-k]]
        else:
            colors[c[i-k]] -= 1
        if len(colors) > max_colors:
            max_colors = len(colors)
    print(max_colors)
