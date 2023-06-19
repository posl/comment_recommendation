def pascal_triangle(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        result = []
        for i in range(1, n + 1):
            if i == 1:
                result.append(1)
            elif i == 2:
                result.append(1)
            else:
                result.append(pascal_triangle(n - 1)[i - 2] + pascal_triangle(n - 1)[i - 3])
        return result
