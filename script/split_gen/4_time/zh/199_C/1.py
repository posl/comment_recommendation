def main():
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        tmp = input().split()
        t.append(int(tmp[0]))
        a.append(int(tmp[1]))
        b.append(int(tmp[2]))
    for i in range(q):
        if t[i] == 1:
            if a[i] <= n and b[i] <= n:
                s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
            elif a[i] <= n and b[i] > n:
                s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:n] + s[n:b[i]-1] + s[a[i]-1] + s[b[i]:]
            elif a[i] > n and b[i] <= n:
                s = s[:n] + s[a[i]-1] + s[n+1:b[i]-1] + s[a[i]-1] + s[b[i]:]
            elif a[i] > n and b[i] > n:
                s = s[:n] + s[a[i]-1] + s[n+1:n] + s[b[i]-1] + s[n+1:a[i]-1] + s[b[i]-1] + s[a[i]:]
        elif t[i] == 2:
            s = s[n:] + s[:n]
    print(s)
