def main():
    n, m = map(int, input().split())
    a = [[0 for i in range(n)] for i in range(m)]
    for i in range(m):
        k = list(map(int, input().split()))
        for j in range(1, k[0] + 1):
            a[i][k[j] - 1] = 1
    for i in range(n):
        for j in range(i + 1, n):
            flag = True
            for k in range(m):
                if a[k][i] == 1 and a[k][j] == 1:
                    flag = False
            if flag:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()