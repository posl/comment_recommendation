def main():
    s = input()
    q = int(input())
    t = [0] * q
    f = [0] * q
    c = [0] * q
    for i in range(q):
        t[i], f[i], c[i] = map(str, input().split())
        t[i] = int(t[i])
        f[i] = int(f[i])
    #print(s, q, t, f, c)
    s = list(s)
    #print(s)
    rev = False
    for i in range(q):
        if t[i] == 1:
            rev = not rev
            #print("rev")
        else:
            if f[i] == 1:
                if rev:
                    s.append(c[i])
                else:
                    s.insert(0, c[i])
            else:
                if rev:
                    s.insert(0, c[i])
                else:
                    s.append(c[i])
            #print("add", s)
    if rev:
        s = s[::-1]
    print("".join(s))
