def solve():
    s1 = input()
    s2 = input()
    if s1[1] == '#' and s2[1] == '#' and s1[0] == '#' and s2[0] == '#':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()