def solution(a, b, c, d):
    result = 0
    for x in range(a, b + 1):
        for y in range(c, d + 1):
            result = max(result, x * y)
    return result

if __name__ == '__main__':
    solution()