def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        if a[i] <= b[i]:
            ans += a[i]
            b[i] -= a[i]
            if a[i + 1] <= b[i]:
                ans += a[i + 1]
                a[i + 1] = 0
            else:
                ans += b[i]
                a[i + 1] -= b[i]
        else:
            ans += b[i]
    print(ans)
