def solve():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    if len(s) == len(t):
        print('No')
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[:i] + s[i + 1:] == t[:i] + t[i + 1:]:
                print('Yes')
                return
            else:
                print('No')
                return
    print('No')

if __name__ == '__main__':
    solve()