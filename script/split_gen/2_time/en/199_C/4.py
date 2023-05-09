def main():
    n = int(input())
    s = input()
    q = int(input())
    t = [0] * q
    a = [0] * q
    b = [0] * q
    for i in range(q):
        t[i], a[i], b[i] = map(int, input().split())
    
    l = [0] * n
    r = [0] * n
    for i in range(n):
        l[i] = i
        r[i] = i + n
    
    for i in range(q):
        if t[i] == 1:
            a[i] -= 1
            b[i] -= 1
            if a[i] < n and b[i] < n:
                l[a[i]], l[b[i]] = l[b[i]], l[a[i]]
            elif a[i] < n and b[i] >= n:
                l[a[i]], r[b[i] - n] = r[b[i] - n], l[a[i]]
            elif a[i] >= n and b[i] < n:
                r[a[i] - n], l[b[i]] = l[b[i]], r[a[i] - n]
            else:
                r[a[i] - n], r[b[i] - n] = r[b[i] - n], r[a[i] - n]
        else:
            l, r = r, l
    
    ans = ""
    for i in range(n):
        ans += s[l[i]]
    for i in range(n):
        ans += s[r[i]]
    print(ans)
