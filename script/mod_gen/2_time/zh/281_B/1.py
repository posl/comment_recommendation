def main():
    s = input()
    if s[0].isupper() and s[-1].isupper():
        s = s[1:-1]
        if len(s) == 6 and s.isdigit() and int(s) >= 100000 and int(s) <= 999999:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()