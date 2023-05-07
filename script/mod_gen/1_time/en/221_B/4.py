def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    s = list(s)
    t = list(t)
    for i in range(len(s)-1):
        s[i], s[i+1] = s[i+1], s[i]
        if s == t:
            print('Yes')
            return
        s[i], s[i+1] = s[i+1], s[i]
    print('No')
    return

if __name__ == '__main__':
    main()