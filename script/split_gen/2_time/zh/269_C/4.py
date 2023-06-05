def solve():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                return i+1, j+1
