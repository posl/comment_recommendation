def main():
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        t_i, a_i, b_i = map(int, input().split())
        t.append(t_i)
        a.append(a_i)
        b.append(b_i)
    for i in range(q):
        if t[i] == 1:
            if a[i] <= n:
                a[i] = a[i] + n
            else:
                a[i] = a[i] - n
            if b[i] <= n:
                b[i] = b[i] + n
            else:
                b[i] = b[i] - n
            s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        else:
            s = s[n:] + s[:n]
    print(s)

if __name__ == '__main__':
    main()