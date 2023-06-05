def main():
    S = input()
    S = S[::-1]
    for i in range(len(S)):
        if S[i] == '6':
            print('9', end='')
        elif S[i] == '9':
            print('6', end='')
        else:
            print(S[i], end='')
    print()

if __name__ == '__main__':
    main()