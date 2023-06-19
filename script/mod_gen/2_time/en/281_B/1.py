def main():
    s = input()
    if s[0].isupper() and s[-1].isupper() and s[1:-1].isdecimal() and 100000 <= int(s[1:-1]) <= 999999:
        print('Yes')
    else:
        print('No')
main()
