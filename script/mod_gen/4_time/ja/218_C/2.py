def rotate(s):
    n = len(s)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = s[i][j]
    return ret

if __name__ == '__main__':
    rotate()