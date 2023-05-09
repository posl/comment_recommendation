def main():
    s = input()
    n = len(s)
    if s == s[::-1]:
        if s[:n//2] == s[:n//2][::-1]:
            if s[n//2+1:] == s[n//2+1:][::-1]:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()