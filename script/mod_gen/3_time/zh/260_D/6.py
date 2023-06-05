def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]-1] = i+1
    import bisect
    a = [0] * n
    b = [0] * n
    c = [0] * n
    t = 0
    for i in range(n):
        x = q[i]
        if i >= k:
            y = q[i-k]
            if y < a[t]:
                t -= 1
            if t > 0:
                u = bisect.bisect_left(b, y)
                if u > 0:
                    t -= 1
                    a[u-1] = a[t]
                    b[u-1] = b[t]
                    c[u-1] = c[t]
            else:
                u = 0
            while u < t and a[u] > x:
                u += 1
            if u < t:
                a[u] = x
                b[u] = y
                c[u] = i
            else:
                a[t] = x
                b[t] = y
                c[t] = i
                t += 1
        else:
            if t > 0:
                u = bisect.bisect_left(b, x)
                if u > 0:
                    t -= 1
                    a[u-1] = a[t]
                    b[u-1] = b[t]
                    c[u-1] = c[t]
            else:
                u = 0
            while u < t and a[u] > x:
                u += 1
            if u < t:
                a[u] = x
                b[u] = x
                c[u] = i
            else:
                a[t] = x
                b[t] = x
                c[t] = i
                t += 1
        if i >= k-1:
            print(c[t-1]+1)
        else:
            print(-1)
main()
