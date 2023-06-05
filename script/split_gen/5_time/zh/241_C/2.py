def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i] = s[i][:j] + '0' + s[i][j+1:]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '0':
                s[i] = s[i][:j] + '#' + s[i][j+1:]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '0':
                s[i] = s[i][:j] + '.' + s[i][j+1:]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i] = s[i][:j] + '0' + s[i][j+1:]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '0':
                s[i] = s[i][:j] + '#' + s[i][j+1:]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '0':
                s[i] = s[i][:j] + '.' + s[i][j+1:]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i] = s[i][:j] + '0' + s[i][j+1:]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '0':
                s[i] = s[i][:j] + '#' + s[i][j+1:]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '0':
                s[i] = s[i][:j] + '.' + s[i][j+1:]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i] = s[i][:j] + '0' + s[i][j+1:]
    for i in range(n):
        for j in range(n):
            if s[i][j] ==
