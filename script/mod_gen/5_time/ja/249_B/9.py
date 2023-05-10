def solve():
    s = input()
    if len(s) != len(set(s)):
        print('No')
        return
    if not s.islower() and not s.isupper():
        print('Yes')
        return
    print('No')

if __name__ == '__main__':
    solve()