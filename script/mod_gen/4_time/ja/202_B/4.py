def main():
    S = input()
    S = list(S)
    for i in range(len(S)):
        if S[i] == '0':
            S[i] = '0'
        elif S[i] == '1':
            S[i] = '1'
        elif S[i] == '6':
            S[i] = '9'
        elif S[i] == '8':
            S[i] = '8'
        elif S[i] == '9':
            S[i] = '6'
    S.reverse()
    print(''.join(S))

if __name__ == '__main__':
    main()