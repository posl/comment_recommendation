def get_path(start, end, parent):
    path = [start]
    while path[-1] != end:
        path.append(parent[path[-1]])
    return path

if __name__ == '__main__':
    get_path()