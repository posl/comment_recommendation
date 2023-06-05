def main():
    s = input()
    t = input()
    if len(s) != len(t):
        return print("No")
    else:
        for i in range(len(s)):
            s = s[-1] + s[:-1]
            if s == t:
                return print("Yes")
        return print("No")

if __name__ == '__main__':
    main()