def pascal_triangle(n):
    if n == 0:
        return [1]
    else:
        prev = pascal_triangle(n-1)
        return [1] + [prev[i]+prev[i+1] for i in range(len(prev)-1)] + [1]

if __name__ == '__main__':
    pascal_triangle()