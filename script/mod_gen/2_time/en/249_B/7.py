def main():
    s = input()
    s = s.upper()
    if len(s) == len(set(s)):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()