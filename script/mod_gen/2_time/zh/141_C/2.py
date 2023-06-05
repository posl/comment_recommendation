def main():
    s = input()
    if s[::2] == s[::2].replace('L', '').replace('U', '').replace('D', '') and s[1::2] == s[1::2].replace('R', '').replace('U', '').replace('D', ''):
        print('Yes')
    else:
        print('No')
main()
