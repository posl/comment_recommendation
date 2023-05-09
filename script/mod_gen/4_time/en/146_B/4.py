def main():
    n = int(input())
    s = input()
    if n == 0:
        print(s)
    else:
        for i in range(len(s)):
            if ord(s[i]) + n > 90:
                print(chr(ord(s[i]) + n - 26), end="")
            else:
                print(chr(ord(s[i]) + n), end="")
        print()

if __name__ == '__main__':
    main()