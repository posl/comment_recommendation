def pascal_triangle(n):
    pascal = [[1]]
    for i in range(n-1):
        new_list = [1]
        for j in range(i):
            new_list.append(pascal[-1][j] + pascal[-1][j+1])
        new_list.append(1)
        pascal.append(new_list)
    return pascal
n = int(input())
pascal = pascal_triangle(n)
for i in range(n):
    print(*pascal[i])
