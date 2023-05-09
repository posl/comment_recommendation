def PascalsTriangle(N):
    triangle = []
    for i in range(N):
        if i == 0:
            triangle.append([1])
        elif i == 1:
            triangle.append([1,1])
        else:
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle.append(row)
    return triangle

if __name__ == '__main__':
    PascalsTriangle()