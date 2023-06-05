def rotate_90(s):
    return [[s[y][x] for y in range(len(s))] for x in range(len(s[0])-1, -1, -1)]

if __name__ == '__main__':
    rotate_90()