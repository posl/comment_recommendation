def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    else:
        for i in range(len(s)-1):
            s = s[:i] + s[i+1] + s[i] + s[i+2:]
            if s == t:
                print("Yes")
                return
            else:
                s = s[:i] + s[i+1] + s[i] + s[i+2:]
        print("No")
        return

if __name__ == '__main__':
    main()