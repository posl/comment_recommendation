def main():
    str = []
    for i in range(9):
        str.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if str[i][j] == '#':
                count += 1
    print(count)

if __name__ == '__main__':
    main()