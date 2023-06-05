def count_visible_square(h, w, x, y, s):
    count = 1
    for i in range(x-1, -1, -1):
        if s[i][y-1] == '#':
            break
        else:
            count += 1
    for i in range(x, h):
        if s[i][y-1] == '#':
            break
        else:
            count += 1
    for i in range(y-2, -1, -1):
        if s[x-1][i] == '#':
            break
        else:
            count += 1
    for i in range(y, w):
        if s[x-1][i] == '#':
            break
        else:
            count += 1
    return count

if __name__ == '__main__':
    count_visible_square()