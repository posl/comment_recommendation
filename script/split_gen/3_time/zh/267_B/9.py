def solve():
    s = input()
    for i in range(10):
        if s[i] == '0':
            if i == 0:
                if s[1] == '1' and s[2] == '1':
                    print('Yes')
                    return
            elif i == 9:
                if s[8] == '1' and s[7] == '1':
                    print('Yes')
                    return
            else:
                if s[i-1] == '1' and s[i+1] == '1':
                    print('Yes')
                    return
    print('No')
solve()
