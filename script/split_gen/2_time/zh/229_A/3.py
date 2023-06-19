def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s2[0] == '#':
        print('Yes')
    elif s1[0] == '#' and s2[0] == '.':
        if s1[1] == '#':
            print('Yes')
        else:
            print('No')
    elif s1[0] == '.' and s2[0] == '#':
        if s2[1] == '#':
            print('Yes')
        else:
            print('No')
    else:
        print('No')
