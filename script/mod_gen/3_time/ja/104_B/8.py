def main():
    s = input()
    if s[0] == "A":
        if s[2:-1].count("C") == 1:
            if s[1:s[2:-1].find("C")+2].islower() and s[s[2:-1].find("C")+3:-1].islower():
                if s[-1].islower():
                    print("AC")
                    exit()
    print("WA")

if __name__ == '__main__':
    main()