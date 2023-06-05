def main():
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        t1, a1, b1 = map(int, input().split())
        t.append(t1)
        a.append(a1)
        b.append(b1)
    s1 = s[:n]
    s2 = s[n:]
    for i in range(q):
        if t[i] == 1:
            if a[i] < n and b[i] < n:
                s1 = s1[:a[i]] + s2[b[i]] + s1[a[i]+1:]
                s2 = s2[:b[i]] + s1[a[i]] + s2[b[i]+1:]
            elif a[i] < n and b[i] >= n:
                s1 = s1[:a[i]] + s2[b[i]-n] + s1[a[i]+1:]
                s2 = s2[:b[i]-n] + s1[a[i]] + s2[b[i]-n+1:]
            elif a[i] >= n and b[i] < n:
                s1 = s1[:a[i]-n] + s2[b[i]] + s1[a[i]-n+1:]
                s2 = s2[:b[i]] + s1[a[i]-n] + s2[b[i]+1:]
            else:
                s1 = s1[:a[i]-n] + s2[b[i]-n] + s1[a[i]-n+1:]
                s2 = s2[:b[i]-n] + s1[a[i]-n] + s2[b[i]-n+1:]
        else:
            s1, s2 = s2, s1
    print(s1+s2)
