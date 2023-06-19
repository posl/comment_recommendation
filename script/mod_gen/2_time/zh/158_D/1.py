def main():
    s = input()
    q = int(input())
    t = []
    f = []
    c = []
    for i in range(q):
        t1 = input().split()
        t.append(int(t1[0]))
        if t1[0] == '2':
            f.append(int(t1[1]))
            c.append(t1[2])
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
        #print(s)
    print(s)

if __name__ == '__main__':
    main()