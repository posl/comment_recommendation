def solve():
    s = input()
    if s[0] == '0':
        print('No')
        return
    for i in range(1, 10):
        if s[i] == '0':
            print('No')
            return
    if s[1] == '0' and s[8] == '0':
        print('No')
        return
    if s[2] == '0' and s[7] == '0':
        print('No')
        return
    if s[3] == '0' and s[6] == '0':
        print('No')
        return
    if s[4] == '0' and s[5] == '0':
        print('No')
        return
    print('Yes')
    return
solve()
