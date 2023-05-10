def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    colors = {}
    for i in range(n):
        if i >= k:
            colors[c[i-k]] -= 1
            if colors[c[i-k]] == 0:
                del colors[c[i-k]]
        if c[i] not in colors:
            colors[c[i]] = 1
        else:
            colors[c[i]] += 1
        ans = max(ans, len(colors))
    print(ans)
