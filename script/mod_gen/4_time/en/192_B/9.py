def main():
    S = input()
    #print(S)
    if S[::2].islower() and S[1::2].isupper():
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()