def main():
    S = input()
    if S[0] == 'A' and 'C' in S[2:-1] and S[1:].islower():
        print('AC')
    else:
        print('WA')
main()
