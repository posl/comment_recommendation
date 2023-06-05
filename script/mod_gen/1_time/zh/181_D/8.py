def main():
    # S = input()
    S = '1234'
    # S = '1333'
    # S = '8'
    if len(S) == 1:
        if S == '8':
            print('yes')
        else:
            print('no')
    elif len(S) == 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print('yes')
        else:
            print('no')
    else:
        if int(S) % 8 == 0:
            print('yes')
        elif int(S[0] + S[2] + S[1]) % 8 == 0:
            print('yes')
        elif int(S[1] + S[0] + S[2]) % 8 == 0:
            print('yes')
        elif int(S[1] + S[2] + S[0]) % 8 == 0:
            print('yes')
        elif int(S[2] + S[0] + S[1]) % 8 == 0:
            print('yes')
        elif int(S[2] + S[1] + S[0]) % 8 == 0:
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    main()