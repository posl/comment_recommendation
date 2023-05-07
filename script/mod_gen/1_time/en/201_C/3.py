def main():
    s = input()
    if s[0] == 'o':
        ans = 9
    else:
        ans = 10
    for i in range(1, 10):
        if s[i] == 'o':
            ans *= 9 - i
        elif s[i] == '?':
            ans *= 10 - i
    print(ans)

if __name__ == '__main__':
    main()