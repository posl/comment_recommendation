def main():
    # input
    S = input()
    # compute
    # output
    if S[0]=='A' and S[2:-1].count('C')==1:
        print('AC')
    else:
        print('WA')

if __name__ == '__main__':
    main()