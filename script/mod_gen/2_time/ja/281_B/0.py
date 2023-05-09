def main():
    s = input()
    if len(s) == 1:
        if s.isupper():
            print("Yes")
        else:
            print("No")
    else:
        if s[0].isupper() and s[-1].isupper():
            if s[1:-1].isdigit():
                if 100000 <= int(s[1:-1]) <= 999999:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")

if __name__ == '__main__':
    main()