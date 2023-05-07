def main():
    s = input()
    print('Yes' if s[0] == '0' and s[1:].count('1') >= 2 else 'No')

if __name__ == '__main__':
    main()