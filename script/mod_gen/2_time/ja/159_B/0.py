def main():
    s = input()
    print('Yes' if s == s[::-1] and s[:(len(s)-1)//2] == s[:(len(s)-1)//2][::-1] and s[(len(s)+3)//2-1:] == s[(len(s)+3)//2-1:][::-1] else 'No')

if __name__ == '__main__':
    main()