def main():
    # s = input()
    # t = input()
    s = 'abbaac'
    t = 'abbbbaaac'
    if len(s) < 2 or len(s) > 2*10**5 or len(t) < 2 or len(t) > 2*10**5:
        print('No')
        return
    if s == t:
        print('Yes')
        return
    if s[0] != t[0]:
        print('No')
        return
    if s[-1] != t[-1]:
        print('No')
        return
    if s[-2] != t[-2]:
        print('No')
        return
    if s[-3] != t[-3]:
        print('No')
        return
    print('Yes')

if __name__ == '__main__':
    main()