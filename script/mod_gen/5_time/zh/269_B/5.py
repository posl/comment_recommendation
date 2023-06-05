def main():
    a = []
    for i in range(10):
        a.append(input())
    for i in range(10):
        if a[0][i] == '#':
            x1 = i
            break
    for i in range(9, -1, -1):
        if a[9][i] == '#':
            x2 = i
            break
    for i in range(10):
        if a[i][0] == '#':
            y1 = i
            break
    for i in range(9, -1, -1):
        if a[i][9] == '#':
            y2 = i
            break
    print(y1+1, x1+1)
    print(y2+1, x2+1)

if __name__ == '__main__':
    main()