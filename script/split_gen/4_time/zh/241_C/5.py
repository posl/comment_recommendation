def main():
    n = int(input())
    s = [input() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i] = s[i][:j] + '1' + s[i][j + 1:]
    for j in range(n):
        for i in range(n):
            if s[i][j] == '#':
                s[i] = s[i][:j] + '1' + s[i][j + 1:]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '.':
                s[i] = s[i][:j] + '0' + s[i][j + 1:]
    for j in range(n):
        for i in range(n):
            if s[i][j] == '.':
                s[i] = s[i][:j] + '0' + s[i][j + 1:]
    for i in range(n):
        s[i] = int(s[i], 2)
    for i in range(n):
        for j in range(n - 5):
            if s[i] >> j & 63 == 0:
                print('Yes')
                return
    for j in range(n):
        for i in range(n - 5):
            if (s[i] >> j & 63) == 0:
                print('Yes')
                return
    for i in range(n - 5):
        for j in range(n - 5):
            if (s[i] >> j & 63) == 0:
                print('Yes')
                return
    for i in range(n - 5):
        for j in range(n - 1, 4, -1):
            if (s[i] >> j & 63) == 0:
                print('Yes')
                return
    print('No')
