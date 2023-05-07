def main():
    S = input()
    if S[0] != 'A':
        print('WA')
        return
    if S[2:-1].count('C') != 1:
        print('WA')
        return
    if len(S) - S[2:-1].count('C') - S.count('A') != 2:
        print('WA')
        return
    print('AC')
main()
