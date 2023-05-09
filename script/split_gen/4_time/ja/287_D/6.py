def solve():
    s = input()
    t = input()
    slen = len(s)
    tlen = len(t)
    if slen < tlen:
        print("No")
        return
    for i in range(tlen):
        if s[i] == "?":
            continue
        if s[i] != t[i]:
            print("No")
            return
    for i in range(tlen, slen):
        if s[i] == "?":
            print("Yes")
            return
        if s[i] != t[tlen-1]:
            print("No")
            return
    print("Yes")
    return
