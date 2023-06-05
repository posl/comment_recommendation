def rotate_90(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for i in range(n):
        for j in range(n//2):
            matrix[i][j],matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]
    return matrix
n = int(input())
s = [list(input()) for i in range(n)]
t = [list(input()) for i in range(n)]
for _ in range(4):
    s = rotate_90(s)
    if s == t:
        print('Yes')
        exit()
print('No')

if __name__ == '__main__':
    rotate_90()