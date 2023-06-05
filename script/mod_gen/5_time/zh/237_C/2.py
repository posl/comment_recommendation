def main():
    s = input()
    a = 'a'
    if s == s[::-1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()