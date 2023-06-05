def check(s):
    if len(s) < 2 or len(s) > 100:
        print("No")
        return
    if s.islower() or s.isupper():
        print("No")
        return
    if s[0].islower() and s[1].isupper():
        print("Yes")
        return
    if s[0].isupper() and s[1].islower():
        print("Yes")
        return
    for i in range(2, len(s)):
        if s[i].islower() and s[i-1].isupper():
            print("Yes")
            return
        if s[i].isupper() and s[i-1].islower():
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    check()