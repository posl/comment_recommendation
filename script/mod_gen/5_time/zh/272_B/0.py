def main():
    n, m = map(int, input().split())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        k, *x = map(int, input().split())
        for j in range(k):
            for l in range(j + 1, k):
                a[x[j] - 1][x[l] - 1] = 1
                a[x[l] - 1][x[j] - 1] = 1
    flag = True
    for i in range(n):
        for j in range(i + 1, n):
            if a[i][j] == 0:
                flag = False
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()