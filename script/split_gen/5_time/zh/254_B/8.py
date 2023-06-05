def pascal_triangle(num):
    tri = []
    for i in range(num):
        tri.append([1]*(i+1))
        for j in range(1,i):
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
    return tri
