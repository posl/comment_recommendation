def main():
    s = input()
    if s[0].isupper() and s[7].isupper() and s[1:7].isdigit() and int(s[1:7])>=100000 and int(s[1:7])<=999999:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()