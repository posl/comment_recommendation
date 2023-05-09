def main():
    s = input()
    ans = ''
    for i in range(len(s)):
        if s[i] == '0':
            ans = '0' + ans
        elif s[i] == '1':
            ans = '1' + ans
        elif s[i] == '6':
            ans = '9' + ans
        elif s[i] == '8':
            ans = '8' + ans
        elif s[i] == '9':
            ans = '6' + ans
    print(ans)

if __name__ == '__main__':
    main()