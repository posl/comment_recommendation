def main():
    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    for x in range(0, lt+1):
        if s[x] == t[x] or s[x] == '?':
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()