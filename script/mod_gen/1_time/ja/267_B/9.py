def main():
    S = input()
    print('Yes' if S[1:].count('1') > 0 and S[:9].count('0') > 0 else 'No')

if __name__ == '__main__':
    main()