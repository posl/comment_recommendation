def solve():
    s = input()
    if s.islower():
        print('No')
        return
    if s.isupper():
        print('No')
        return
    if len(s) % 2 != 0:
        print('No')
        return
    print('Yes')

if __name__ == '__main__':
    solve()