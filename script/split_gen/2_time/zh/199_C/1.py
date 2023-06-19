def solve():
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
    flag = False
    for i in range(q-1, -1, -1):
        if t[i] == 1:
            if flag:
                if a[i] <= n:
                    a[i] += n
                else:
                    a[i] -= n
                if b[i] <= n:
                    b[i] += n
                else:
                    b[i] -= n
            s = s[0:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
        else:
            flag = not flag
    if flag:
        s = s[n:] + s[:n]
    print(s)
