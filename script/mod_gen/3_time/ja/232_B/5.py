def main():
    s = input()
    t = input()
    for k in range(26):
        for i in range(len(s)):
            if ord(t[i]) - ord(s[i]) != k and ord(t[i]) - ord(s[i]) != k - 26:
                break
        else:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()