def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                continue
            s[i] = s[i][:j] + '#' + s[i][j+1:]
            if check(s):
                print('Yes')
                return
            s[i] = s[i][:j] + '.' + s[i][j+1:]
    print('No')
