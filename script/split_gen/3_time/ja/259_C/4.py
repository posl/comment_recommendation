def main():
    s = input()
    t = input()
    slen = len(s)
    tlen = len(t)
    if slen > tlen:
        print("No")
        exit()
    if slen == tlen:
        if s == t:
            print("Yes")
        else:
            print("No")
        exit()
    if slen < tlen:
        i = 0
        j = 0
        while i < slen:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == slen:
            print("Yes")
        else:
            print("No")
        exit()
