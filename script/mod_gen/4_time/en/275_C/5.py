def main():
    s = [input() for i in range(9)]
    print(s)
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                count += 1
    print(count)

if __name__ == '__main__':
    main()