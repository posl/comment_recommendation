def main():
    n, m, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a = sorted(a)
    b = sorted(b)
    ans = 0
    while a or b:
        if a and b:
            if a[0] < b[0]:
                if k < a[0]:
                    break
                k -= a[0]
                ans += 1
                a.pop(0)
            else:
                if k < b[0]:
                    break
                k -= b[0]
                ans += 1
                b.pop(0)
        elif a:
            if k < a[0]:
                break
            k -= a[0]
            ans += 1
            a.pop(0)
        else:
            if k < b[0]:
                break
            k -= b[0]
            ans += 1
            b.pop(0)
    print(ans)
