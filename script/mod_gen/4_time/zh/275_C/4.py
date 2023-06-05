def main():
    s = []
    for i in range(9):
        s.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i == 0:
                    if j == 0:
                        if s[i+1][j] == '#' and s[i][j+1] == '#' and s[i+1][j+1] == '#':
                            count += 1
                    elif j == 8:
                        if s[i+1][j] == '#' and s[i][j-1] == '#' and s[i+1][j-1] == '#':
                            count += 1
                    else:
                        if s[i+1][j] == '#' and s[i][j-1] == '#' and s[i][j+1] == '#' and s[i+1][j-1] == '#' and s[i+1][j+1] == '#':
                            count += 1
                elif i == 8:
                    if j == 0:
                        if s[i-1][j] == '#' and s[i][j+1] == '#' and s[i-1][j+1] == '#':
                            count += 1
                    elif j == 8:
                        if s[i-1][j] == '#' and s[i][j-1] == '#' and s[i-1][j-1] == '#':
                            count += 1
                    else:
                        if s[i-1][j] == '#' and s[i][j-1] == '#' and s[i][j+1] == '#' and s[i-1][j-1] == '#' and s[i-1][j+1] == '#':
                            count += 1
                else:
                    if j == 0:
                        if s[i-1][j] == '#' and s[i+1][j] == '#' and s[i][j+1] == '#' and s[i-1][j+1] == '#' and s[i+1][j+1] == '#':
                            count += 1
                    elif j == 8:
                        if s[i-1][j] == '#' and s[i+1][j] == '#' and s[i][j-1] == '#' and s[i-1][j

if __name__ == '__main__':
    main()