def main():
    s = input()
    t = input()
    if s == t:
        print(0)
        exit()
    if len(s) != len(t):
        print(-1)
        exit()
    if len(s) == 1:
        print(1)
        exit()
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    if ans == 2:
        print(2)
    else:
        print(-1)
main()

if __name__ == '__main__':
    main()