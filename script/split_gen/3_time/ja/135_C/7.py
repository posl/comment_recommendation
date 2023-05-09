def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] - b[i] >= 0:
            ans += b[i]
            a[i] -= b[i]
        else:
            ans += a[i]
            b[i] -= a[i]
            a[i] = 0
            if a[i+1] - b[i] >= 0:
                ans += b[i]
                a[i+1] -= b[i]
            else:
                ans += a[i+1]
                a[i+1] = 0
    print(ans)
