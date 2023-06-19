def main():
    n, m = map(int, input().split())
    b = []
    for i in range(n):
        b.append(list(map(int, input().split())))
    for i in range(1, n):
        for j in range(m):
            if b[i][j] != b[i-1][j]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()