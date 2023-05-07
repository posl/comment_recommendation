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
    s1 = s[:n]
    s2 = s[n:]
    for i in range(q):
        if t[i] == 2:
            s1, s2 = s2, s1
        else:
            if a[i] <= n:
                if b[i] <= n:
                    s1 = s1[:a[i] - 1] + s1[b[i] - 1] + s1[a[i]:b[i] - 1] + s1[a[i] - 1] + s1[b[i]:]
                else:
                    s1 = s1[:a[i] - 1] + s2[b[i] - n - 1] + s1[a[i]:]
                    s2 = s2[:b[i] - n - 1] + s1[a[i] - 1] + s2[b[i] - n:]
            else:
                if b[i] <= n:
                    s2 = s2[:a[i] - n - 1] + s1[b[i] - 1] + s2[a[i] - n:]
                    s1 = s1[:b[i] - 1] + s2[a[i] - n - 1] + s1[b[i]:]
                else:
                    s2 = s2[:a[i] - n - 1] + s2[b[i] - n - 1] + s2[a[i] - n:b[i] - n - 1] + s2[a[i] - n - 1] + s2[b[i] - n:]
    print(s1 + s2)
main()

if __name__ == '__main__':
    main()