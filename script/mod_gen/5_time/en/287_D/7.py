def main():
    s = input()
    t = input()
    slen = len(s)
    tlen = len(t)
    for i in range(tlen+1):
        if s[:i] == t[:i] and s[slen-tlen+i:] == t[i:]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()