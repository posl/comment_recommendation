def main():
    S = input()
    if S[0] == '0':
        print('No')
    else:
        if S[1] == '1' and S[2] == '1':
            print('No')
        elif S[3] == '1' and S[4] == '1':
            print('No')
        elif S[5] == '1' and S[6] == '1':
            print('No')
        elif S[7] == '1' and S[8] == '1':
            print('No')
        elif S[9] == '1' and S[0] == '1':
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()