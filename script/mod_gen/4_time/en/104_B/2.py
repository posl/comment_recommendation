def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(len(s)):
            if s[i] != 'A' and s[i] != 'C':
                if s[i].isupper():
                    print("WA")
                    exit()
        print("AC")
    else:
        print("WA")

if __name__ == '__main__':
    main()