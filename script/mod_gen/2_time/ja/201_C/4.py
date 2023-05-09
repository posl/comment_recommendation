def main():
    s = input()
    ans = 0
    if s[0] == 'o':
        ans = 10000
    elif s[0] == 'x':
        ans = 0
    else:
        ans = 9999
    for i in range(1, len(s)):
        if s[i] == 'o':
            ans *= 9 - i
        elif s[i] == 'x':
            ans *= 0
        else:
            ans *= 10 - i
    print(ans)

if __name__ == '__main__':
    main()