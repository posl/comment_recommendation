def main():
    s = input()
    if s[0] == "A" and s[2:-1].count("C") == 1:
        cnt = 0
        for i in range(len(s)):
            if s[i].isupper():
                cnt += 1
        if cnt == 2:
            print("AC")
            return
    print("WA")
    return

if __name__ == '__main__':
    main()