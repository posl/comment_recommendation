def findPath(n, m, a, b):
    if n == 1:
        return [1]
    elif n == 2:
        return [-1]
    else:
        result = [0] * n
        result[0] = 1
        result[1] = 2
        result[2] = 3
        for i in range(3, n):
            result[i] = i + 1
        for i in range(m):
            if a[i] == 1 and b[i] == 2:
                return [-1]
            elif a[i] == 1:
                result[b[i] - 1] = 1
                result[1] = b[i]
            elif b[i] == 1:
                result[a[i] - 1] = 2
                result[0] = a[i]
            else:
                result[a[i] - 1] = b[i]
                result[b[i] - 1] = a[i]
        return result

if __name__ == '__main__':
    findPath()