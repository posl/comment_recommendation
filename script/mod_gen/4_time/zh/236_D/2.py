def main():
    n = int(input())
    a = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            a[i][j] = int(input())
    print(a)

if __name__ == '__main__':
    main()