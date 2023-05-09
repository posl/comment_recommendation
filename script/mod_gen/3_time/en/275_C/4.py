def main():
    a = []
    for i in range(9):
        a.append(input())
    count = 0
    for i in range(7):
        for j in range(7):
            if a[i][j] == '#' and a[i + 1][j] == '#' and a[i][j + 1] == '#' and a[i + 1][j + 1] == '#':
                count += 1
    print(count)

if __name__ == '__main__':
    main()