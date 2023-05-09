def main():
    s = input()
    ans = ""
    for i in range(len(s)):
        if s[i] == '6':
            ans = '9' + ans
        elif s[i] == '9':
            ans = '6' + ans
        else:
            ans = s[i] + ans
    print(ans)

if __name__ == '__main__':
    main()