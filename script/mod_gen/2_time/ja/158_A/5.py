def main():
    s = input()
    print("Yes" if s[0] != s[1] or s[1] != s[2] or s[0] != s[2] else "No")

if __name__ == '__main__':
    main()