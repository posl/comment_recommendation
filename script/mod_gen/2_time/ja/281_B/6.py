def main():
    s = input()
    if s[0].isupper() and s[-1].isupper():
        if len(s) >= 2:
            if s[1:].isdecimal():
                if int(s[1:]) >= 100000 and int(s[1:]) <= 999999:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()