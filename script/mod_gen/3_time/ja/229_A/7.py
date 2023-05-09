def main():
    S = [input() for i in range(2)]
    if S[0][0] == '#' and S[1][0] == '#' or S[0][1] == '#' and S[1][1] == '#' or S[0][0] == '#' and S[0][1] == '#' or S[1][0] == '#' and S[1][1] == '#':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()