def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n):
        s[i] = s[i].replace('.', '0')
        s[i] = s[i].replace('#', '1')
        s[i] = s[i].replace('0', '.')
        s[i] = s[i].replace('1', '#')
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i] = s[i].replace(s[i][j], '1')
            else:
                s[i] = s[i].replace(s[i][j], '0')
    for i in range(n):
        for j in range(n):
            if s[j][i] == '#':
                s[j] = s[j].replace(s[j][i], '1')
            else:
                s[j] = s[j].replace(s[j][i], '0')
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i] = s[i].replace(s[i][j], '1')
            else:
                s[i] = s[i].replace(s[i][j], '0')
    for i in range(n):
        for j in range(n):
            if s[j][i] == '#':
                s[j] = s[j].replace(s[j][i], '1')
            else:
                s[j] = s[j].replace(s[j][i], '0')
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i] = s[i].replace(s[i][j], '1')
            else:
                s[i] = s[i].replace(s[i][j], '0')
    for i in range(n):
        for j in range(n):
            if s[j][i] == '#':
                s[j] = s[j].replace(s[j][i], '1')
            else:
                s[j] = s[j].replace(s[j][i], '0')
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i] = s[i].replace(s[i][j], '1')
            else:
                s[i] = s[i].

if __name__ == '__main__':
    main()