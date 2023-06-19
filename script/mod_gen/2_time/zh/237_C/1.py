def main():
    s = input()
    l = len(s)
    for i in range(l):
        if s[i] != s[l-i-1]:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()