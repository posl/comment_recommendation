def main():
    s = input()
    if s[0].isupper() and s[-1].isupper() and s[1:-1].isdigit() and len(s[1:-1]) == 6 and int(s[1:-1]) >= 100000 and int(s[1:-1]) <= 999999:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()