def main():
    s = input()
    s_reverse = s[::-1]
    s_reverse = 'a' + s_reverse
    if s == s_reverse:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()