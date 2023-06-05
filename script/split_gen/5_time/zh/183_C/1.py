def all_path(n):
    all_path = []
    for i in range(1,n):
        for j in range(i+1,n+1):
            path = [i,j]
            all_path.append(path)
    return all_path
