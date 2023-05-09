def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    colors = set(c[:K])
    max_colors = len(colors)
    for i in range(1, N-K+1):
        colors.remove(c[i-1])
        colors.add(c[i+K-1])
        max_colors = max(max_colors, len(colors))
    print(max_colors)
