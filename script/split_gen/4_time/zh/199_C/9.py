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
    #print(t)
    #print(a)
    #print(b)
    #print(s)
    s1 = s[:n]
    s2 = s[n:]
    for i in range(q):
        if t[i] == 1:
            if a[i] <= n and b[i] <= n:
                s1 = s1[:a[i]-1] + s2[b[i]-1] + s1[a[i]:]
                s2 = s2[:b[i]-1] + s1[a[i]-1] + s2[b[i]:]
            elif a[i] > n and b[i] > n:
                s2 = s2[:a[i]-n-1] + s1[b[i]-n-1] + s2[a[i]-n:]
                s1 = s1[:b[i]-n-1] + s2[a[i]-n-1] + s1[b[i]-n:]
            else:
                s1 = s1[:a[i]-1] + s2[b[i]-n-1] + s1[a[i]:]
                s2 = s2[:b[i]-n-1] + s1[a[i]-1] + s2[b[i]-n:]
        else:
            s1, s2 = s2, s1
    print(s1 + s2)
