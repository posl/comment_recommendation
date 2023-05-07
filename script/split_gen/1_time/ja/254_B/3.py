def main():
    n = int(input())
    a = [[1 for i in range(0, j + 1)] for j in range(0, n)]
    for i in range(1, n):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    for i in range(0, n):
        for j in range(0, i + 1):
            print(a[i][j], end = ' ')
        print()
