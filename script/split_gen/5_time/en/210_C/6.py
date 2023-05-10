def get_max_colors(N, K, c):
    max_colors = 0
    for i in range(N-K+1):
        max_colors = max(max_colors, len(set(c[i:i+K])))
    return max_colors
