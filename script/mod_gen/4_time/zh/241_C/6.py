def check(n, s):
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                if j < n - 5 and s[i][j:j+6] == '######':
                    return True
                if i < n - 5 and s[i][j] == '#' and s[i+1][j] == '#' and s[i+2][j] == '#' and s[i+3][j] == '#' and s[i+4][j] == '#' and s[i+5][j] == '#':
                    return True
                if i < n - 5 and j < n - 5 and s[i][j] == '#' and s[i+1][j+1] == '#' and s[i+2][j+2] == '#' and s[i+3][j+3] == '#' and s[i+4][j+4] == '#' and s[i+5][j+5] == '#':
                    return True
    return False
n = int(input())
s = []
for i in range(n):
    s.append(input())

if __name__ == '__main__':
    check()