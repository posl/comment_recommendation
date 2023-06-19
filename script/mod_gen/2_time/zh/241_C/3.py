def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i] = s[i][:j] + '1' + s[i][j+1:]
    for i in range(n):
        for j in range(n):
            if s[j][i] == '#':
                s[j] = s[j][:i] + '1' + s[j][i+1:]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '1':
                s[i] = s[i][:j] + '0' + s[i][j+1:]
    for i in range(n):
        for j in range(n):
            if s[j][i] == '1':
                s[j] = s[j][:i] + '0' + s[j][i+1:]
    count = 0
    for i in range(n):
        count += s[i].count('0')
    if count >= 6:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()