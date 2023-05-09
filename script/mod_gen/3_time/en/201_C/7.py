def main():
    s = input()
    l = len(s)
    if s[0] == 'x':
        print(0)
        return
    if s[0] == '?':
        ans = 9
    else:
        ans = 1
    for i in range(1,l):
        if s[i] == 'x':
            print(0)
            return
        if s[i] == '?':
            ans *= 9
        elif s[i] == 'o':
            ans *= 1
    print(ans)

if __name__ == '__main__':
    main()