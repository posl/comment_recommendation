def main():
    s = input()
    q = int(input())
    t = []
    f = []
    c = []
    for i in range(q):
        temp = input().split()
        t.append(int(temp[0]))
        if t[i] == 2:
            f.append(int(temp[1]))
            c.append(temp[2])
    r = 0
    for i in range(q):
        if t[i] == 1:
            r += 1
    r = r % 2
    for i in range(q):
        if t[i] == 2:
            if f[i] == 1:
                if r == 0:
                    s = c[i] + s
                else:
                    s = s + c[i]
            else:
                if r == 0:
                    s = s + c[i]
                else:
                    s = c[i] + s
        else:
            r = 1 - r
    if r == 1:
        s = s[::-1]
    print(s)

if __name__ == '__main__':
    main()