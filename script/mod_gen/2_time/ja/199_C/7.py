def main():
    n = int(input())
    s = input()
    q = int(input())
    t, a, b = [], [], []
    for i in range(q):
        ti, ai, bi = map(int, input().split())
        t.append(ti)
        a.append(ai)
        b.append(bi)
    for i in range(q):
        if t[i] == 1:
            s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        else:
            s = s[n:] + s[:n]
    print(s)

if __name__ == '__main__':
    main()