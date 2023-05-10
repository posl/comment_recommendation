def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    slen = len(s)
    tlen = len(t)
    if slen > tlen:
        print("No")
        return
    for i in range(tlen-slen+1):
        if s == t[i:i+slen]:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()