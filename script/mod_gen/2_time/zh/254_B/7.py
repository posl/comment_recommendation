def pascal_triangle(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1],[1,1]]
    else:
        new_line = [1]
        result = pascal_triangle(n-1)
        last_line = result[-1]
        for i in range(len(last_line)-1):
            new_line.append(last_line[i]+last_line[i+1])
        new_line.append(1)
        result.append(new_line)
        return result
n = int(input())
result = pascal_triangle(n)
for line in result:
    print(" ".join(str(x) for x in line))

if __name__ == '__main__':
    pascal_triangle()