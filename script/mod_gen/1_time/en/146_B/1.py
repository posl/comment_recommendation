def main():
    n = int(input())
    s = input()
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            print(chr(ord(s[i]) + n - 26), end="")
        else:
            print(chr(ord(s[i]) + n), end="")

if __name__ == '__main__':
    main()