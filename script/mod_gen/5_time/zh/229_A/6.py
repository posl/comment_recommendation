def main():
    s_1 = input()
    s_2 = input()
    if s_1[0] == '#' and s_1[1] == '#' and s_2[0] == '#' and s_2[1] == '#':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()