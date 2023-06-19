def main():
    s = input().split()
    t = input().split()
    if s[0] == t[0] and s[1] == t[1] and s[2] == t[2]:
        print("Yes")
    elif s[0] == t[0] and s[1] == t[2] and s[2] == t[1]:
        print("Yes")
    elif s[0] == t[1] and s[1] == t[0] and s[2] == t[2]:
        print("Yes")
    elif s[0] == t[1] and s[1] == t[2] and s[2] == t[0]:
        print("Yes")
    elif s[0] == t[2] and s[1] == t[0] and s[2] == t[1]:
        print("Yes")
    elif s[0] == t[2] and s[1] == t[1] and s[2] == t[0]:
        print("Yes")
    else:
        print("No")
main()
