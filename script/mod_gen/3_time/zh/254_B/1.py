def f():
    n = int(input())
    a = [[0 for j in range(i+1)] for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                a[i][j] = 1
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        print(' '.join(map(str, a[i])))

if __name__ == '__main__':
    f()