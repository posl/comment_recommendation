def solve():
    S = input()
    if S.find('o') == -1 or S.find('x') == -1:
        print('Yes')
        return
    if S.find('o') < S.find('x'):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()