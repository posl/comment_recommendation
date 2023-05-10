def main():
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] != "a":
            if s[i] == "t":
                cnt += 1
            elif s[i] == "c":
                cnt += 1
            elif s[i] == "o":
                cnt += 1
            elif s[i] == "d":
                cnt += 1
            elif s[i] == "e":
                cnt += 1
            elif s[i] == "r":
                cnt += 1
            else:
                cnt += 2
    print(cnt)

if __name__ == '__main__':
    main()