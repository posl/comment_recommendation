def get_all_paths(start, graph, visited, n):
    if len(visited) == n:
        return [[start]]
    paths = []
    for i in range(n):
        if i not in visited:
            visited.append(i)
            paths += [[start] + path for path in get_all_paths(i, graph, visited, n)]
            visited.pop()
    return paths

if __name__ == '__main__':
    get_all_paths()