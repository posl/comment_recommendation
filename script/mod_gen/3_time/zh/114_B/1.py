def get_min_diff(s):
    min_diff = 999
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        diff = abs(753-x)
        if diff < min_diff:
            min_diff = diff
    return min_diff

if __name__ == '__main__':
    get_min_diff()