def pascal_triangle(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    else:
        a = [1]
        b = pascal_triangle(n-1)
        for i in range(len(b)-1):
            a.append(b[i]+b[i+1])
        a.append(1)
        return a
n = int(input())
for i in range(1,n+1):
    print(*pascal_triangle(i))

if __name__ == '__main__':
    pascal_triangle()