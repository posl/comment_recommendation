def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if (ord(t[i])-ord(s[i]))%26 != 0:
            print("No")
            return
    print("Yes")
    return
main()
