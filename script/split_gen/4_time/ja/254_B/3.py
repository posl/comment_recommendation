def main():
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    a[0][0] = 1
    for i in range(1, n):
        a[i][0] = 1
        a[i][i] = 1
        for j in range(1, i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        print(" ".join([str(a[i][j]) for j in range(i+1)]))
