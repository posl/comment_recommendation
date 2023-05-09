def main():
    s = input()
    ans = ''
    for i in range(len(s)):
        ans += s[len(s)-1-i]
    ans = ans.replace('6', 'x')
    ans = ans.replace('9', '6')
    ans = ans.replace('x', '9')
    ans = ans.replace('0', 'x')
    ans = ans.replace('1', '0')
    ans = ans.replace('x', '1')
    print(ans)

if __name__ == '__main__':
    main()