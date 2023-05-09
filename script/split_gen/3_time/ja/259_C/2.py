def solve():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        exit()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s = s[:i+1] + s[i] + s[i+1:]
            if s == t:
                print("Yes")
                exit()
    print("No")
