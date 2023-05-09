def pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        line = [1]
        triangle = pascal_triangle(n-1)
        last_line = triangle[-1]
        for i in range(len(last_line)-1):
            line.append(last_line[i] + last_line[i+1])
        line += [1]
        triangle.append(line)
    return triangle
n = int(input())
triangle = pascal_triangle(n)
for line in triangle:
    print(" ".join(map(str, line)))
