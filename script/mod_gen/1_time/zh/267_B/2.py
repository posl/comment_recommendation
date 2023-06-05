def solve():
    s = input()
    if s[0] == '0':
        return 'No'
    if s[3] == '0':
        return 'No'
    if s[4] == '0':
        return 'No'
    if s[7] == '0':
        return 'No'
    if s[9] == '0':
        return 'No'
    return 'Yes'

if __name__ == '__main__':
    solve()