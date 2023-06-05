def count_visible(x, y, h, w, s):
    count = 0
    for i in range(h):
        if s[i][y - 1] == ".":
            count += 1
    for j in range(w):
        if s[x - 1][j] == ".":
            count += 1
    return count - 1

if __name__ == '__main__':
    count_visible()