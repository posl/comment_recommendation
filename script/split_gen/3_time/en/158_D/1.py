def main():
    s = input()
    q = int(input())
    t = []
    f = []
    c = []
    for i in range(q):
        t_i = input().split()
        t.append(int(t_i[0]))
        if t_i[0] == '2':
            f.append(int(t_i[1]))
            c.append(t_i[2])
    s = list(s)
    for i in range(q):
        if t[i] == 1:
            s.reverse()
        else:
            if f[i] == 1:
                s.insert(0, c[i])
            else:
                s.append(c[i])
    print(''.join(s))
