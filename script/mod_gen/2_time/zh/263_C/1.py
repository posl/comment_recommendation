def dfs(start, depth, max_depth, parents):
    if depth > max_depth:
        max_depth = depth
    if start in parents:
        max_depth = dfs(parents[start], depth+1, max_depth, parents)
    return max_depth

if __name__ == '__main__':
    dfs()