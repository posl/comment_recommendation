def main():
    # input
    S = input()
    # compute
    if S[0] != 'A':
        print('WA')
        return
    if S[2:-1].count('C') != 1:
        print('WA')
        return
    if S[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')

if __name__ == '__main__':
    main()