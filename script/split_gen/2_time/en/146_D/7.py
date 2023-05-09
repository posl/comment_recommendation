def main():
    N = int(input())
    # 1-indexed
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    # 1-indexed
    colors = [0] * (N+1)
    # 1-indexed
    used = [0] * (N+1)
    # 1-indexed
    for i in range(1, N+1):
        # 0-indexed
        for j in range(len(edges)):
            if i in edges[j]:
                # 1-indexed
                for k in range(1, N+1):
                    # 0-indexed
                    if k in edges[j]:
                        used[colors[k]] = 1
                # 0-indexed
                for k in range(1, N+1):
                    if used[k] == 0:
                        colors[i] = k
                        break
                # 0-indexed
                for k in range(1, N+1):
                    if k in edges[j]:
                        used[colors[k]] = 0
    print(max(colors))
    # 0-indexed
    for i in range(N-1):
        print(colors[edges[i][0]])
