def main():
    s = input()
    if s[0] != "A":
        print("WA")
        return
    if s[2:-1].count("C") != 1:
        print("WA")
        return
    if s[1] == "C" or s[-1] == "C":
        print("WA")
        return
    for c in s[1:]:
        if c != "C" and c.isupper():
            print("WA")
            return
    print("AC")

if __name__ == '__main__':
    main()