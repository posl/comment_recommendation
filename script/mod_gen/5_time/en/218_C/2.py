def rotate90(a):
    n = len(a)
    b = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            b[j][n-1-i] = a[i][j]
    return b

if __name__ == '__main__':
    rotate90()