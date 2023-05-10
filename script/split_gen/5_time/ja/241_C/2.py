def main():
    n = int(input())
    s = [input() for _ in range(n)]
    #print(s)
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                continue
            else:
                s[i] = s[i][:j] + 'X' + s[i][j+1:]
    #print(s)
    for i in range(n):
        for j in range(n):
            if s[j][i] == '#':
                continue
            else:
                s[j] = s[j][:i] + 'X' + s[j][i+1:]
    #print(s)
    for i in range(n):
        for j in range(n):
            if s[i][j] == 'X':
                continue
            else:
                s[i] = s[i][:j] + '.' + s[i][j+1:]
    #print(s)
    for i in range(n):
        for j in range(n):
            if s[j][i] == 'X':
                continue
            else:
                s[j] = s[j][:i] + '.' + s[j][i+1:]
    #print(s)
    for i in range(n):
        if 'X' in s[i]:
            print('No')
            exit()
    print('Yes')
