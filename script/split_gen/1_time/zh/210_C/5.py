def main():
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))
    colors = {}
    for i in range(k):
        if candies[i] in colors.keys():
            colors[candies[i]] += 1
        else:
            colors[candies[i]] = 1
    max_colors = len(colors.keys())
    for i in range(k, n):
        if candies[i] in colors.keys():
            colors[candies[i]] += 1
        else:
            colors[candies[i]] = 1
        if colors[candies[i-k]] == 1:
            del colors[candies[i-k]]
        else:
            colors[candies[i-k]] -= 1
        max_colors = max(max_colors, len(colors.keys()))
    print(max_colors)
