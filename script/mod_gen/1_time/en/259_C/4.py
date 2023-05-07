def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    i = 0
    while i < len(s):
        if i == len(t):
            print("Yes")
            return
        if s[i] == t[i]:
            i += 1
        else:
            if i + 1 < len(s) and s[i] == s[i + 1]:
                s = s[:i] + s[i + 1:]
            else:
                print("No")
                return
    if i == len(t):
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()