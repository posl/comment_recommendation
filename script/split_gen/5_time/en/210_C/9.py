def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    # print(n, k)
    # print(c)
    candies = c[:k]
    # print(candies)
    colors = set(candies)
    # print(colors)
    max_colors = len(colors)
    # print(max_colors)
    for i in range(k, n):
        candies.pop(0)
        candies.append(c[i])
        colors = set(candies)
        # print(colors)
        max_colors = max(max_colors, len(colors))
        # print(max_colors)
    print(max_colors)
