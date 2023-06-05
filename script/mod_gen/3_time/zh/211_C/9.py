def main():
    s = input()
    mod = 1000000007
    num = [0] * 8
    for i in range(len(s)):
        if s[i] == 'c':
            num[0] += 1
        elif s[i] == 'h':
            num[1] += num[0]
            num[1] %= mod
        elif s[i] == 'o':
            num[2] += num[1]
            num[2] %= mod
        elif s[i] == 'k':
            num[3] += num[2]
            num[3] %= mod
        elif s[i] == 'u':
            num[4] += num[3]
            num[4] %= mod
        elif s[i] == 'd':
            num[5] += num[4]
            num[5] %= mod
        elif s[i] == 'a':
            num[6] += num[5]
            num[6] %= mod
        elif s[i] == 'i':
            num[7] += num[6]
            num[7] %= mod
    print(num[7])

if __name__ == '__main__':
    main()