def main():
    s = input()
    t = input()
    slen = len(s)
    tlen = len(t)
    for i in range(tlen+1):
        s1 = s[0:i]
        s2 = s[i+tlen:slen]
        if s1.replace('?', 'a') + t + s2.replace('?', 'a') == s:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()