def main():
    s = input()
    if s[0] != "A":
        print("WA")
        return
    if s[2:-1].count("C") != 1:
        print("WA")
        return
    if s[1:].replace("C", "").islower():
        print("AC")
    else:
        print("WA")
    return

if __name__ == '__main__':
    main()