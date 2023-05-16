def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    if len(s) == len(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[:i] == t[:i] and s[i+1:] == t[i:]:
                print("Yes")
                return
            else:
                print("No")
                return
    print("No")

if __name__ == '__main__':
    main()