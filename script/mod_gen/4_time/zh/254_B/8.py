def pascal_triangle(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1],[1,1]]
    else:
        new_line = [1]
        last_line = pascal_triangle(n-1)[-1]
        for i in range(len(last_line)-1):
            new_line.append(last_line[i]+last_line[i+1])
        new_line.append(1)
        return pascal_triangle(n-1)+[new_line]

if __name__ == '__main__':
    pascal_triangle()