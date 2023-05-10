def solve():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)-1):
        if s[i:i+2] == t[i:i+2][::-1]:
            print("Yes")
            return
    print("No")
