def main():
    s = input()
    if len(s) != 3:
        print("Input must be a string of length 3")
        return
    if s[0] == s[1] and s[1] == s[2]:
        print(-1)
        return
    elif s[0] == s[1]:
        print(s[2])
        return
    elif s[1] == s[2]:
        print(s[0])
        return
    elif s[0] == s[2]:
        print(s[1])
        return
    else:
        print(s[0])
        return

if __name__ == '__main__':
    main()