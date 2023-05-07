def main():
    s = input()
    if len(s) == 1:
        print(1)
        return
    ans = 0
    for i in range(len(s)-1):
        if s[i] == '0':
            ans += 1
        else:
            ans += 2
    if s[-1] == '0':
        ans += 1
    else:
        ans += 2
    print(ans)

if __name__ == '__main__':
    main()