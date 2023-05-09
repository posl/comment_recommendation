def pascals_triangle(n):
    if n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascals_triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result
n = int(input())
for i in pascals_triangle(n):
    print(*i)

if __name__ == '__main__':
    pascals_triangle()