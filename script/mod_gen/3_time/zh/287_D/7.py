def main():
    s = input()
    t = input()
    tlen = len(t)
    slen = len(s)
    s1 = s.replace('?','a')
    s2 = s.replace('?','z')
    if tlen == slen:
        if t == s1:
            print('Yes')
        else:
            print('No')
    else:
        for i in range(slen-tlen+1):
            if t == s1[i:i+tlen] or t == s2[i:i+tlen]:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()