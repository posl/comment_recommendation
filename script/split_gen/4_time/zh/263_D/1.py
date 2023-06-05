def main():
    n,l,r = map(int, input().split())
    a = list(map(int, input().split()))
    if l > r:
        l,r = r,l
    if l >= 0:
        ans = sum(a) + l * n
    elif r <= 0:
        ans = sum(a) + r * n
    else:
        ans = sum(a)
        m = 0
        for i in range(n):
            if a[i] < 0:
                if l + a[i] < 0:
                    m += (l + a[i])
                    a[i] = 0
                else:
                    a[i] += l
        if m < 0:
            for i in range(n):
                if a[i] > 0:
                    if r + a[i] > 0:
                        m += (r + a[i])
                        a[i] = 0
                    else:
                        a[i] += r
                if m >= 0:
                    break
        ans += m
    print(ans)
