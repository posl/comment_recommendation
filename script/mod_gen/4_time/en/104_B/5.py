def main():
    s = input()
    if s[0] == "A" and s[2:-1].count("C") == 1:
        for c in s:
            if c == "A" or c == "C":
                continue
            elif c.isupper():
                print("WA")
                exit()
        print("AC")
    else:
        print("WA")

if __name__ == '__main__':
    main()