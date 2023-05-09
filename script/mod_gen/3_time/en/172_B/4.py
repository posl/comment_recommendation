def main():
    s = input()
    t = input()
    l = len(s)
    ans = 0
    for i in range(l):
        if s[i] != t[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()