def main():
    s = input()
    s1 = s[::-1]
    if s == s1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()