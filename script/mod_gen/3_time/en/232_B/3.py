def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        if s[i] == 'a':
            if t[i] == 'z':
                continue
            else:
                print("No")
                return
        if ord(s[i]) - ord(t[i]) == 1:
            continue
        else:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()