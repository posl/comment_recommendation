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
    #print(s)
    #print(q)
    #print(t)
    #print(f)
    #print(c)
    for i in range(q):
        if t[i] == 1:
            s = s[::-1]
        else:
            if f[i] == 1:
                s = c[i] + s
            else:
                s = s + c[i]
    print(s)

if __name__ == '__main__':
    main()