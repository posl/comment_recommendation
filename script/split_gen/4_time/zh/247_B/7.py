def check(n, namelist):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if namelist[i][0] == namelist[j][0] or namelist[i][0] == namelist[j][1] or namelist[i][1] == namelist[j][0] or namelist[i][1] == namelist[j][1]:
                return False
    return True
