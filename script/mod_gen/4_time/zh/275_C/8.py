def main():
    s = []
    for i in range(9):
        s.append(input())
    #print(s)
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i+1 < 9 and j+1 < 9:
                    if s[i+1][j] == '#' and s[i][j+1] == '#' and s[i+1][j+1] == '#':
                        count += 1
    print(count)

if __name__ == '__main__':
    main()