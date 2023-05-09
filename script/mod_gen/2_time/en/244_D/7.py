def main():
    s = list(input().split())
    t = list(input().split())
    if s == t:
        print("Yes")
    elif s[0] == t[0] and s[1] == t[1]:
        print("Yes")
    elif s[1] == t[1] and s[2] == t[2]:
        print("Yes")
    elif s[2] == t[2] and s[0] == t[0]:
        print("Yes")
    elif s[0] == t[0] and s[2] == t[2]:
        print("Yes")
    elif s[1] == t[1] and s[0] == t[0]:
        print("Yes")
    elif s[2] == t[2] and s[1] == t[1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()