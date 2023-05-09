def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if t[i] == s[i]:
            continue
        if t[i] == "a" and s[i] == "z":
            continue
        if t[i] == "z" and s[i] == "a":
            continue
        if t[i] == "b" and s[i] == "y":
            continue
        if t[i] == "y" and s[i] == "b":
            continue
        if t[i] == "c" and s[i] == "x":
            continue
        if t[i] == "x" and s[i] == "c":
            continue
        if ord(t[i]) - ord(s[i]) == 1:
            continue
        if ord(s[i]) - ord(t[i]) == 1:
            continue
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()