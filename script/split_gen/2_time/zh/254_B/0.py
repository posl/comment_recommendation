def main():
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2, n):
        for j in range(1, i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(a[i][j], end=" ")
        print()
