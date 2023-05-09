def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        exit()
    if len(s) + 1 != len(t):
        print("No")
        exit()
    if s[0] != t[0]:
        print("No")
        exit()
    if s[-1] != t[-1]:
        print("No")
        exit()
    s = s[1:-1]
    t = t[1:-1]
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            exit()
    print("Yes")
