def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        s1 = s[:i]
        s2 = s[-(len(t)-i):]
        if '?' in s1:
            s1 = s1.replace('?', 'a')
        if '?' in s2:
            s2 = s2.replace('?', 'a')
        if s1+s2 == t:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()