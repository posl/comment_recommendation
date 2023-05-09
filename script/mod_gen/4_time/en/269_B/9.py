def main():
    s = []
    for i in range(10):
        s.append(input())
    # print(s)
    for i in range(10):
        if s[i].count('.') == 10:
            row = i
            break
    # print(row)
    for i in range(10):
        if s[i][row] == '#':
            col = i
            break
    # print(col)
    for i in range(row):
        if s[col][i] == '#':
            row -= 1
        else:
            break
    # print(row)
    for i in range(col):
        if s[i][row] == '#':
            col -= 1
        else:
            break
    # print(col)
    print(col + 1, row + 1)

if __name__ == '__main__':
    main()