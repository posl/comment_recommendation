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
    s = list(s)
    for i in range(q):
        if t[i] == 1:
            s.reverse()
        elif t[i] == 2:
            if f[i] == 1:
                s.insert(0, c[i])
            elif f[i] == 2:
                s.append(c[i])
    print(''.join(s))
