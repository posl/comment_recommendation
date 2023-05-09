def main():
    s = input()
    if s == s[::-1] and s[:len(s)//2] == s[:len(s)//2][::-1] and s[len(s)//2+1:] == s[len(s)//2+1:][::-1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()