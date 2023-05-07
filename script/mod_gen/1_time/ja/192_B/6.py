def main():
    S = input()
    print('Yes' if S[0::2].islower() and S[1::2].isupper() else 'No')

if __name__ == '__main__':
    main()