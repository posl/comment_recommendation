def main():
    S = input()
    print('Yes' if S[0] == '0' and S[1:].count('1') >= 2 else 'No')

if __name__ == '__main__':
    main()