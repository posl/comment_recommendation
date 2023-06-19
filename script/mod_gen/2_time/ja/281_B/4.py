def main():
    s = input()
    if s[0].isalpha() and s[-1].isalpha():
        if len(s) == 2:
            print('Yes')
        else:
            if s[1:-1].isdigit() and 100000 <= int(s[1:-1]) <= 999999:
                print('Yes')
            else:
                print('No')
    else:
        print('No')
main()
