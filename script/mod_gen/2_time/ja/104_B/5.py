def main():
    S = input()
    if len(S) < 4 or len(S) > 10:
        print('WA')
        return
    if S[0] != 'A':
        print('WA')
        return
    if S[2:-1].count('C') != 1:
        print('WA')
        return
    S = S.replace('A', '')
    S = S.replace('C', '')
    if S.islower():
        print('AC')
    else:
        print('WA')

if __name__ == '__main__':
    main()