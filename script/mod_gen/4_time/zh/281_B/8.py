def main():
    s = input()
    if s[0].isupper() and s[-1].isupper() and len(s) == 8:
        if s[1:7].isdigit():
            if int(s[1:7]) >= 100000 and int(s[1:7]) <= 999999:
                print("Yes")
                return
    print("No")
    return

if __name__ == '__main__':
    main()