def solve():
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
    isFront = True
    for i in range(q-1, -1, -1):
        if t[i] == 1:
            if isFront:
                if a[i] <= n and b[i] <= n:
                    s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:b[i]-1] + s[a[i]-1] + s[b[i]:]
                elif a[i] <= n and n < b[i]:
                    s = s[:a[i]-1] + s[b[i]-1] + s[a[i]:n] + s[n-1] + s[n:b[i]-1] + s[a[i]-1] + s[b[i]:]
                elif n < a[i] and b[i] <= 2*n:
                    s = s[:n] + s[a[i]-1-n] + s[n:a[i]-1] + s[b[i]-1-n] + s[a[i]-1:b[i]-1] + s[b[i]-n:]
                elif n < a[i] and 2*n < b[i]:
                    s = s[:n] + s[a[i]-1-n] + s[n:a[i]-1] + s[b[i]-1-n] + s[a[i]-1:n] + s[b[i]-1] + s[n:b[i]-n-1] + s[b[i]-n:]
            else:
                if a[i] <= n and b[i] <= n:
                    s = s[:a[i]-1+n] + s[b[i]-1+n] + s[a[i]-1+n+1:b[i]-1+n] + s[a[i]-1+n] + s[b[i]-1+n+1:]
                elif a[i] <= n and n < b[i]:
                    s = s[:a[i]-1+n] + s[b[i]-1] + s[a[i]-1+n+1:n] + s[b[i]-1+n] + s[a[i]-1:n-1] + s[b[i]-1

if __name__ == '__main__':
    solve()