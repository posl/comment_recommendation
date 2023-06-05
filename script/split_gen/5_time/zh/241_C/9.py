def main():
    n = int(input())
    s = [input() for _ in range(n)]
    #print(s)
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                continue
            s[i] = s[i][:j] + '#' + s[i][j+1:]
            for k in range(n):
                if s[k][j] == '#':
                    continue
                s[k] = s[k][:j] + '#' + s[k][j+1:]
                for l in range(n):
                    if s[k][l] == '#':
                        continue
                    s[k] = s[k][:l] + '#' + s[k][l+1:]
                    #print(s)
                    if check(s):
                        print('Yes')
                        return
                    s[k] = s[k][:l] + '.' + s[k][l+1:]
                s[k] = s[k][:j] + '.' + s[k][j+1:]
            s[i] = s[i][:j] + '.' + s[i][j+1:]
    print('No')
    return
