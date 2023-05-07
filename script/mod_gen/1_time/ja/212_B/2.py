def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Weak")
    else:
        if (int(s[0]) + 1) % 10 == int(s[1]) and (int(s[1]) + 1) % 10 == int(s[2]) and (int(s[2]) + 1) % 10 == int(s[3]):
            print("Weak")
        else:
            print("Strong")

if __name__ == '__main__':
    main()