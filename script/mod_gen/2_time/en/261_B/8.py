def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(input()))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == 'W' and a[j][i] == 'L':
                continue
            if a[i][j] == 'L' and a[j][i] == 'W':
                continue
            if a[i][j] == 'D' and a[j][i] == 'D':
                continue
            print('incorrect')
            return
    print('correct')

if __name__ == '__main__':
    main()