def main():
    n = int(input())
    s = [input() for _ in range(n)]
    # print(n)
    # print(s)
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i] = s[i][:j] + '1' + s[i][j+1:]
            else:
                s[i] = s[i][:j] + '0' + s[i][j+1:]
    # print(s)
    for i in range(n):
        for j in range(n):
            if s[i][j] == '1':
                s[i] = s[i][:j] + '0' + s[i][j+1:]
                if s[i].count('1') >= 6:
                    print('Yes')
                    return
                s[i] = s[i][:j] + '1' + s[i][j+1:]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '1':
                s[i] = s[i][:j] + '0' + s[i][j+1:]
                for k in range(n):
                    if s[k][j] == '1':
                        s[k] = s[k][:j] + '0' + s[k][j+1:]
                        if s[k].count('1') >= 6:
                            print('Yes')
                            return
                        s[k] = s[k][:j] + '1' + s[k][j+1:]
                s[i] = s[i][:j] + '1' + s[i][j+1:]
    print('No')
