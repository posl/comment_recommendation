def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()