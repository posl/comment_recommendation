def find_min_diff(x, p):
    min_diff = 100
    for i in range(0, 101):
        if i not in p:
            if abs(x - i) < min_diff:
                min_diff = abs(x - i)
                result = i
    return result

if __name__ == '__main__':
    find_min_diff()