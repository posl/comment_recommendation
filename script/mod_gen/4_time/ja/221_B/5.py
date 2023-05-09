def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)-1):
        s = list(s)
        s[i], s[i+1] = s[i+1], s[i]
        s = "".join(s)
        if s == t:
            print("Yes")
            return
        else:
            s = list(s)
            s[i], s[i+1] = s[i+1], s[i]
            s = "".join(s)
    print("No")

if __name__ == '__main__':
    main()