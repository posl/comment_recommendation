def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    if sorted(s) != sorted(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] in t[i + 1:]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()