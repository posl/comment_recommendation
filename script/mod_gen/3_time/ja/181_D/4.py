def main():
    S = input()
    if '8' in S:
        if int(S) % 8 == 0:
            print('Yes')
        else:
            if int(S[1:]) % 8 == 0:
                print('Yes')
            else:
                if int(S[1:]+S[0]) % 8 == 0:
                    print('Yes')
                else:
                    print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()