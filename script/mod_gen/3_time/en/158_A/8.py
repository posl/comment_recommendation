def solve():
    s = input()
    if s.count('A') == 1 or s.count('B') == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()