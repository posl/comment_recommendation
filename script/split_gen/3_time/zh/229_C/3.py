def main():
    n,w = input().split()
    n = int(n)
    w = int(w)
    a = []
    b = []
    for i in range(n):
        ai,bi = input().split()
        a.append(int(ai))
        b.append(int(bi))
    #print(a)
    #print(b)
    ans = 0
    for i in range(n):
        #print(i)
        #print(w)
        #print(a[i])
        #print(b[i])
        if w - a[i] >= 0:
            ans += a[i] * b[i]
            w -= a[i]
        else:
            ans += w * b[i]
            w = 0
        if w == 0:
            break
    print(ans)
main()
