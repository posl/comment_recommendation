def main():
    s = input()
    for i in range(0,len(s)):
        if i%2 == 0:
            if s[i].isupper():
                print('No')
                return
        else:
            if s[i].islower():
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()