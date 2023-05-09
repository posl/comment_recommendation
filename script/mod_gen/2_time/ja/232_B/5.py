def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                if ord(s[i]) + 1 == ord(t[i]):
                    continue
                elif ord(s[i]) + 1 == ord("z") and ord(t[i]) == ord("a"):
                    continue
                else:
                    print("No")
                    return
        print("Yes")

if __name__ == '__main__':
    main()