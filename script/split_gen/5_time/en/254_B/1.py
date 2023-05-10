def pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascal_triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result
n = int(input())
triangle = pascal_triangle(n)
for row in triangle:
    for item in row:
        print(item, end=' ')
    print()
