def main():
    # input
    S = input()
    # compute
    # output
    if S[0::2].count('L') + S[0::2].count('R') + S[1::2].count('U') + S[1::2].count('D') == len(S):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()