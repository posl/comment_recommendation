def solve():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[2] == '#' or s2[0] == '#' and s2[2] == '#':
        print('Yes')
    else:
        print('No')
