def main():
    h,w = map(int,input().split())
    s = [input() for i in range(h)]
    t = [input() for i in range(h)]
    s2 = []
    t2 = []
    for i in range(h):
        s2.append("".join(sorted(s[i])))
        t2.append("".join(sorted(t[i])))
    s2.sort()
    t2.sort()
    for i in range(h):
        if s2[i] != t2[i]:
            print("No")
            return
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                if t[i][j] == "#":
                    print("No")
                    return
                else:
                    for k in range(h):
                        if s[k][j] == "#":
                            print("No")
                            return
                    break
    print("Yes")
    return

if __name__ == '__main__':
    main()